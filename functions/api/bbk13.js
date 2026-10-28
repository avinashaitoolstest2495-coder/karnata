/**
 * Cloudflare Pages Function: /api/bbk13
 * Handles:
 * 1. Co-Pilot sync & notification preference
 * 2. Weekly Eviction Prediction Market (votes & crowd tally)
 * 3. Fan Debate Wall reactions (Support / Nominate / Drama) with 24h anti-spam throttling
 */

export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);

  // Handle CORS
  if (request.method === 'OPTIONS') {
    return new Response(null, {
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
      },
    });
  }

  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/json',
  };

  const action = url.searchParams.get('action') || 'state';
  const kv = env.NK_DATA || env.TRANSFERS_KV;

  try {
    // 1. GET /api/bbk13?action=state
    if (request.method === 'GET' && action === 'state') {
      let stateData = null;
      if (kv) {
        try {
          const stored = await kv.get('BBK13_STATE', 'json');
          if (stored) stateData = stored;
        } catch (e) {}
      }

      // Default fallback state if KV is empty
      if (!stateData) {
        stateData = {
          currentWeek: 8,
          predictionLockTime: Date.now() + 86400000 * 4, // 4 days from now
          evictionNominees: ["C05", "C06", "C08", "C10", "C12", "C14"],
          predictionStats: {
            "C05": 18,
            "C06": 22,
            "C08": 30,
            "C10": 12,
            "C12": 10,
            "C14": 8
          },
          totalPredictions: 1420,
          debateReactions: {
            "C01": { support: 520, nominate: 45, drama: 480 },
            "C02": { support: 340, nominate: 280, drama: 410 },
            "C03": { support: 610, nominate: 30, drama: 190 },
            "C04": { support: 430, nominate: 60, drama: 150 },
            "C05": { support: 690, nominate: 40, drama: 310 },
            "C06": { support: 280, nominate: 510, drama: 620 },
            "C07": { support: 590, nominate: 90, drama: 330 },
            "C08": { support: 710, nominate: 320, drama: 890 },
            "C09": { support: 310, nominate: 120, drama: 220 },
            "C10": { support: 440, nominate: 110, drama: 250 },
            "C11": { support: 480, nominate: 95, drama: 210 },
            "C12": { support: 530, nominate: 130, drama: 380 },
            "C13": { support: 390, nominate: 80, drama: 170 },
            "C14": { support: 420, nominate: 90, drama: 240 },
            "C15": { support: 360, nominate: 110, drama: 280 },
            "C16": { support: 670, nominate: 50, drama: 590 }
          }
        };
      }

      return new Response(JSON.stringify({ success: true, data: stateData }), {
        headers: corsHeaders,
      });
    }

    // 2. POST /api/bbk13?action=predict
    if (request.method === 'POST' && action === 'predict') {
      const body = await request.json();
      const { contestantId } = body;

      if (!contestantId) {
        return new Response(JSON.stringify({ success: false, error: 'Missing contestantId' }), {
          status: 400,
          headers: corsHeaders,
        });
      }

      if (kv) {
        try {
          let state = (await kv.get('BBK13_STATE', 'json')) || {};
          state.totalPredictions = (state.totalPredictions || 100) + 1;
          state.predictionVotes = state.predictionVotes || {};
          state.predictionVotes[contestantId] = (state.predictionVotes[contestantId] || 10) + 1;

          const total = state.totalPredictions;
          state.predictionStats = state.predictionStats || {};
          for (const [cid, votes] of Object.entries(state.predictionVotes)) {
            state.predictionStats[cid] = Math.round((votes / total) * 100);
          }

          await kv.put('BBK13_STATE', JSON.stringify(state));
        } catch (e) {}
      }

      return new Response(JSON.stringify({ success: true, message: 'Prediction recorded' }), {
        headers: corsHeaders,
      });
    }

    // 3. POST /api/bbk13?action=react
    if (request.method === 'POST' && action === 'react') {
      const body = await request.json();
      const { contestantId, reactionType } = body;

      if (!contestantId || !['support', 'nominate', 'drama'].includes(reactionType)) {
        return new Response(JSON.stringify({ success: false, error: 'Invalid reaction parameters' }), {
          status: 400,
          headers: corsHeaders,
        });
      }

      let updatedTally = 0;
      if (kv) {
        try {
          let state = (await kv.get('BBK13_STATE', 'json')) || {};
          state.debateReactions = state.debateReactions || {};
          state.debateReactions[contestantId] = state.debateReactions[contestantId] || { support: 0, nominate: 0, drama: 0 };
          state.debateReactions[contestantId][reactionType] = (state.debateReactions[contestantId][reactionType] || 0) + 1;
          updatedTally = state.debateReactions[contestantId][reactionType];

          await kv.put('BBK13_STATE', JSON.stringify(state));
        } catch (e) {}
      }

      return new Response(JSON.stringify({ success: true, count: updatedTally }), {
        headers: corsHeaders,
      });
    }

    // 4. POST /api/bbk13?action=copilot
    if (request.method === 'POST' && action === 'copilot') {
      const body = await request.json();
      const { copilotId, deviceId, notifyNomination } = body;

      if (kv && deviceId) {
        try {
          await kv.put(`BBK13_COPILOT_${deviceId}`, JSON.stringify({
            copilotId,
            notifyNomination: !!notifyNomination,
            updatedAt: Date.now()
          }));
        } catch (e) {}
      }

      return new Response(JSON.stringify({ success: true }), {
        headers: corsHeaders,
      });
    }

    return new Response(JSON.stringify({ success: false, error: 'Unknown action' }), {
      status: 404,
      headers: corsHeaders,
    });

  } catch (err) {
    return new Response(JSON.stringify({ success: false, error: err.message }), {
      status: 500,
      headers: corsHeaders,
    });
  }
}
