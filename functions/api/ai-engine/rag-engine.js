/**
 * Ask Karnata AI — Retrieval-Augmented Generation (RAG) Context Builder
 * Gathers relevant D1 document chunks and state facts to strictly ground the LLM.
 */

export async function buildRAGContext(normalizedQ, intent, env) {
  let docContext = '';

  // 1. Query relevant documents from D1
  if (env && env.DB) {
    try {
      const tokens = normalizedQ.split(' ').filter(t => t.length > 2);
      let querySql = 'SELECT title, content, source_url FROM ai_documents LIMIT 3';
      let params = [];

      if (tokens.length > 0) {
        const conditions = tokens.map(() => '(title LIKE ? OR content LIKE ? OR keywords LIKE ?)').join(' OR ');
        querySql = `SELECT title, content, source_url FROM ai_documents WHERE category = ? OR ${conditions} LIMIT 3`;
        params.push(intent);
        tokens.forEach(t => {
          params.push(`%${t}%`);
          params.push(`%${t}%`);
          params.push(`%${t}%`);
        });
      }

      const rows = await env.DB.prepare(querySql).bind(...params).all();
      if (rows && rows.results && rows.results.length > 0) {
        docContext = rows.results.map(r => `[DOC: ${r.title}]\n${r.content}`).join('\n\n');
      }
    } catch (dbErr) {
      console.warn('[RAG Document Retrieval Warning]:', dbErr);
    }
  }

  // 2. Structured Grounding Facts
  const verifiedFacts = `
STATE LEADERSHIP (KARNATAKA, INDIA):
- Chief Minister: Shri D.K. Shivakumar (INC, Kanakapura)
- Deputy Chief Minister: Dr. G. Parameshwara (INC, Koratagere)
- Governor: Shri Thaawarchand Gehlot
- Chief Secretary: Dr. Shalini Rajneesh, IAS
- Total Assembly Constituencies: 224 | Total Lok Sabha Seats: 28 | Total Districts: 31

5 GUARANTEE SCHEMES:
1. Gruha Lakshmi: ₹2,000/month DBT to female head of family.
2. Gruha Jyothi: Up to 200 units free domestic electricity.
3. Shakti Scheme: Free travel for women in state RTC buses (KSRTC, BMTC, NWKRTC, KKRTC).
4. Anna Bhagya: 10kg free foodgrains/cash equivalent per BPL cardholder.
5. Yuva Nidhi: ₹3,000/month for unemployed graduates, ₹1,500/month for diploma holders.

SIR & ELECTORAL ROLL RULES (ECI):
- Special Summary Revision (SIR) updates voter rolls annually across 224 ACs.
- Form 6: New voter registration (age 18+).
- Form 7: Objections / deletion of deceased or shifted voters.
- Form 8: Correction of particulars, photo update, EPIC replacement, or address shifting.
- Official ECI Portal: voters.eci.gov.in | CEO Karnataka: ceokarnataka.kar.nic.in
`;

  return {
    docContext: docContext || 'No specific document found.',
    verifiedFacts
  };
}
