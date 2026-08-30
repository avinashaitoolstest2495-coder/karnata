/**
 * functions/api/voter-search.js
 * Cloudflare Pages Function for Official ECI Voter Search (EPIC ID & Name)
 * Connects securely to Election Commission of India Gateway (gateway-voters.eci.gov.in)
 */

const ECI_PUBLIC_KEY_B64 = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArb7++BxL/YN8OIln+6FL9Gnw5DNmQ/VFZXss+J+TuQyJc891JbqbijxYQNEin2c2u+CnpXpoGQ/1gUSzDMJeNS3sNSlIUykp2dt7xIm/cmV4sZ/c769vCxVRosMfRaZJnBAah+m1X26lEhnOo0wpAB9Txr8RIyBe6h7PiQWykeJeh6UacOBBX28kgkq7+vJhW8HgB38lt32XRocznRYwS9LqR7ZweFmQhTr1+EGrqiEKCOCxMYgHR2SQckb96hZ9kWzfzeun4bUO5oXKJciLkiS1IgKieADEvYLgu129ZIpn1H+8H+8ikNNVETqEDDMtqcQcQmWppJvcWHaXAs+f8QIDAQAB";
const ECI_RESPONSE_KEY_RAW = "SFfIO0YsOlOKawZe855n97lc4tcPkj7WWsi38yNWpalLBLZzQdkqHWYbZ0=GhSJk2raUo".slice(15, 59);

function base64ToUint8(str) {
  const binary = atob(str);
  const bytes = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i++) {
    bytes[i] = binary.charCodeAt(i);
  }
  return bytes;
}

function uint8ToBase64(bytes) {
  let binary = '';
  const len = bytes.byteLength;
  for (let i = 0; i < len; i++) {
    binary += String.fromCharCode(bytes[i]);
  }
  return btoa(binary);
}

// Decrypt ECI Gateway response (AES-GCM)
async function decryptECIResponse(encryptedB64) {
  if (!encryptedB64 || typeof encryptedB64 !== 'string') return encryptedB64;
  const rawBytes = base64ToUint8(encryptedB64);
  const iv = rawBytes.slice(0, 12);
  const ciphertext = rawBytes.slice(12);

  const keyBytes = base64ToUint8(ECI_RESPONSE_KEY_RAW);
  const key = await crypto.subtle.importKey(
    "raw",
    keyBytes,
    { name: "AES-GCM" },
    false,
    ["decrypt"]
  );

  const decryptedBuf = await crypto.subtle.decrypt(
    { name: "AES-GCM", iv },
    key,
    ciphertext
  );

  const jsonStr = new TextDecoder().decode(decryptedBuf);
  return JSON.parse(jsonStr);
}

// Encrypt payload for ECI Gateway (RSA-OAEP + AES-GCM)
async function encryptECIRequest(payload) {
  const spkiBytes = base64ToUint8(ECI_PUBLIC_KEY_B64);
  const rsaKey = await crypto.subtle.importKey(
    "spki",
    spkiBytes,
    { name: "RSA-OAEP", hash: "SHA-256" },
    false,
    ["encrypt"]
  );

  const aesKeyBytes = crypto.getRandomValues(new Uint8Array(32));
  const ivBytes = crypto.getRandomValues(new Uint8Array(12));

  const aesKey = await crypto.subtle.importKey(
    "raw",
    aesKeyBytes,
    "AES-GCM",
    false,
    ["encrypt"]
  );

  const encodedPayload = new TextEncoder().encode(JSON.stringify(payload));
  const encryptedPayloadBuf = await crypto.subtle.encrypt(
    { name: "AES-GCM", iv: ivBytes },
    aesKey,
    encodedPayload
  );

  const encryptedKeyBuf = await crypto.subtle.encrypt(
    { name: "RSA-OAEP" },
    rsaKey,
    aesKeyBytes
  );

  return {
    encryptedPayload: uint8ToBase64(new Uint8Array(encryptedPayloadBuf)),
    encryptedKey: uint8ToBase64(new Uint8Array(encryptedKeyBuf)),
    iv: uint8ToBase64(ivBytes)
  };
}

export async function onRequest(context) {
  const { request } = context;
  const url = new URL(request.url);

  // CORS Headers
  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, applicationName, appName',
    'Content-Type': 'application/json'
  };

  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders });
  }

  // 1. GET: Fetch Captcha
  if (request.method === 'GET' || url.searchParams.get('action') === 'captcha') {
    try {
      const eciResp = await fetch('https://gateway-voters.eci.gov.in/api/v1/captcha-service/getCaptcha/sir', {
        headers: {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
          'Accept': 'application/json',
          'applicationName': 'ELECTORAL-SEARCH',
          'channelidobo': 'ELECTORAL-SEARCH',
          'appName': 'ELECTORAL-SEARCH'
        }
      });

      if (!eciResp.ok) {
        throw new Error(`ECI Captcha server returned status ${eciResp.status}`);
      }

      const resJson = await eciResp.json();
      if (!resJson || !resJson.data) {
        throw new Error("Invalid response format from ECI captcha service");
      }

      const decrypted = await decryptECIResponse(resJson.data);
      return new Response(JSON.stringify({
        success: true,
        captchaId: decrypted.id,
        captchaImg: `data:image/jpeg;base64,${decrypted.captcha}`
      }), { headers: corsHeaders });

    } catch (err) {
      return new Response(JSON.stringify({
        success: false,
        error: `Unable to load official captcha: ${err.message}`
      }), { status: 500, headers: corsHeaders });
    }
  }

  // 2. POST: Execute Search (by EPIC or by Details/Name)
  if (request.method === 'POST') {
    try {
      const body = await request.json();
      const { searchType, captchaId, captchaData } = body;

      if (!captchaId || !captchaData || !captchaData.trim()) {
        return new Response(JSON.stringify({
          success: false,
          error: "Please enter the security captcha code."
        }), { status: 400, headers: corsHeaders });
      }

      let targetEndpoint = '';
      let payload = {};

      if (searchType === 'epic') {
        const { epicNumber } = body;
        if (!epicNumber || !epicNumber.trim()) {
          return new Response(JSON.stringify({
            success: false,
            error: "Please enter a valid EPIC / Voter ID number."
          }), { status: 400, headers: corsHeaders });
        }

        targetEndpoint = 'https://gateway-voters.eci.gov.in/api/v1/elastic/search-by-epic-from-national-display-v1';
        payload = {
          epicNumber: epicNumber.trim().toUpperCase(),
          stateCd: "S10",
          isPortal: true,
          captchaId: captchaId,
          captchaData: captchaData.trim(),
          securityKey: "na",
          eSEARCHYNEFjd3S: "1021"
        };

      } else if (searchType === 'details' || searchType === 'name') {
        const { applicantFirstName, firstName, applicantLastName, lastName, districtCd, districtNo, acNumber, acNo, relationFirstName, relationName, gender } = body;
        
        const fName = (firstName || applicantFirstName || '').trim();
        const lName = (lastName || applicantLastName || '').trim();
        const rName = (relationName || relationFirstName || '').trim();

        if (!fName) {
          return new Response(JSON.stringify({
            success: false,
            error: "Please enter the elector's first name."
          }), { status: 400, headers: corsHeaders });
        }

        targetEndpoint = 'https://gateway-voters.eci.gov.in/api/v1/elastic/search-by-details-from-state-display-v1';
        
        let distCodeStr = "";
        const rawDist = districtCd || districtNo;
        if (rawDist) {
          const s = rawDist.toString();
          distCodeStr = s.startsWith("S10") ? s : `S10${s.padStart(2, '0')}`;
        }

        const rawAc = acNo || acNumber;
        const acVal = rawAc ? parseInt(rawAc, 10) : "";

        payload = {
          stateCd: "S10",
          firstName: fName,
          lastName: lName,
          relationName: rName,
          relationLastName: "",
          gender: gender || "",
          age: "",
          dob: "",
          birthYear: "",
          districtCd: distCodeStr,
          acNo: acVal,
          isPortal: true,
          captchaId: captchaId,
          captchaData: captchaData.trim(),
          securityKey: "na",
          eSEARCHYNEFjd3S: "1021"
        };

      } else {
        return new Response(JSON.stringify({
          success: false,
          error: "Invalid search type specified."
        }), { status: 400, headers: corsHeaders });
      }

      // Encrypt payload for ECI
      const encryptedReq = await encryptECIRequest(payload);

      // Call official ECI Gateway
      const eciResp = await fetch(targetEndpoint, {
        method: 'POST',
        headers: {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
          'Accept': 'application/json, text/plain, */*',
          'Referer': 'https://electoralsearch.eci.gov.in/',
          'Origin': 'https://electoralsearch.eci.gov.in',
          'applicationName': 'ELECTORAL-SEARCH',
          'channelidobo': 'ELECTORAL-SEARCH',
          'appName': 'ELECTORAL-SEARCH',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(encryptedReq)
      });

      if (eciResp.status === 400) {
        return new Response(JSON.stringify({
          success: false,
          error: "Captcha code was incorrect or expired. Please re-enter the fresh captcha shown."
        }), { headers: corsHeaders });
      }

      if (eciResp.status === 429) {
        return new Response(JSON.stringify({
          success: false,
          error: "ECI server is busy. Please wait a few seconds and try again."
        }), { headers: corsHeaders });
      }

      if (!eciResp.ok) {
        return new Response(JSON.stringify({
          success: false,
          error: `ECI Search Gateway returned HTTP ${eciResp.status}. Please try again.`
        }), { headers: corsHeaders });
      }

      const resJson = await eciResp.json();
      let records = [];

      if (Array.isArray(resJson)) {
        records = resJson;
      } else if (resJson.data) {
        try {
          const decryptedData = await decryptECIResponse(resJson.data);
          records = Array.isArray(decryptedData) ? decryptedData : (decryptedData.content || [decryptedData]);
        } catch (decErr) {
          console.error("Decryption error:", decErr);
        }
      }

      // Normalize results
      const results = records.map(item => {
        const c = item.content || item;
        const acNum = c.acNumber || c.acNo || "";
        const partNum = c.partNumber || c.partNo || "";
        return {
          epicNumber: c.epicNumber || c.epicNo || "",
          name: `${c.applicantFirstName || c.firstName || ''} ${c.applicantLastName || c.lastName || ''}`.trim(),
          nameKn: `${c.applicantFirstNameL1 || c.firstNameL1 || ''} ${c.applicantLastNameL1 || c.lastNameL1 || ''}`.trim(),
          relativeName: `${c.relationFirstName || c.relationName || ''} ${c.relationLastName || c.relationLName || ''}`.trim(),
          relativeNameKn: `${c.relationFirstNameL1 || c.relationNameL1 || ''} ${c.relationLastNameL1 || c.relationLNameL1 || ''}`.trim(),
          relationType: c.relationType || "Relative",
          gender: c.gender || "",
          age: c.age || "",
          state: "Karnataka",
          stateCd: c.stateCd || "S10",
          districtName: c.districtValue || c.districtName || "",
          districtCd: c.districtCd || "",
          acNumber: acNum,
          acName: c.asmblyName || c.acName || "",
          acNameKn: c.asmblyNameL1 || c.acNameL1 || "",
          partNumber: partNum,
          partName: c.partName || "",
          partNameKn: c.partNameL1 || "",
          serialNumber: c.partSerialNumber || c.slnoInpart || "",
          pollingStation: c.psName || c.psBuildingName || c.partName || "",
          pollingStationKn: c.psNameL1 || c.psBuildingNameL1 || c.partNameL1 || "",
          officialPdfUrl: `https://voters.eci.gov.in/download-eroll?stateCode=S10`
        };
      });

      return new Response(JSON.stringify({
        success: true,
        count: results.length,
        results: results
      }), { headers: corsHeaders });

    } catch (err) {
      return new Response(JSON.stringify({
        success: false,
        error: `Search error: ${err.message}`
      }), { status: 500, headers: corsHeaders });
    }
  }

  return new Response("Method not allowed", { status: 405 });
}
