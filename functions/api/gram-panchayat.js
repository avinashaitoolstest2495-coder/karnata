export async function onRequestGet(context) {
  const { request } = context;
  const url = new URL(request.url);
  const gpId = url.searchParams.get('id') || '1520001005';

  const panchatantraUrl = 'https://panchatantra.karnataka.gov.in/USER_MODULE/gpDashboard/getOperationWebService?serviceName=getStaffDetailsForBeforeLogin&serviceType=MASTER';
  
  try {
    const res = await fetch(panchatantraUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        zp_id: gpId.slice(0, 4),
        tp_id: gpId.slice(0, 7),
        gp_id: gpId,
        access_level: '4'
      })
    });

    if (res.ok) {
      const envelope = await res.json();
      const rawStaff = typeof envelope.responseData === 'string' ? JSON.parse(envelope.responseData) : envelope.responseData;
      
      return new Response(JSON.stringify({
        gp_id: gpId,
        source: 'Panchatantra Karnataka Official',
        staff: Array.isArray(rawStaff) ? rawStaff : [],
        total_staff: Array.isArray(rawStaff) ? rawStaff.length : 0,
        retrieved_at: new Date().toISOString()
      }), {
        headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' }
      });
    }
  } catch (e) {}

  return new Response(JSON.stringify({
    gp_id: gpId,
    status: 'empty',
    staff: []
  }), {
    headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' }
  });
}
