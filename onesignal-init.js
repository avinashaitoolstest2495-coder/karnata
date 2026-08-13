/**
 * onesignal-init.js
 * Karnata — OneSignal Web Push initialization
 *
 * SETUP STEPS (do this before going live):
 * 1. Sign up free at https://onesignal.com (free tier covers this use case)
 * 2. Create a new app → Web Push → enter karnata.in as your site URL
 * 3. OneSignal gives you an App ID (looks like: 8cf5c8e8-xxxx-xxxx-xxxx-xxxxxxxxxxxx)
 * 4. Paste it below, replacing YOUR_ONESIGNAL_APP_ID
 * 5. Also download the two worker files OneSignal provides and place them
 *    at your site root as OneSignalSDKWorker.js (they handle background push)
 *
 * This file ONLY sets up the SDK. The actual "ask for permission" UI
 * and district-tagging logic live in index.html (requestPushPermission,
 * tagOneSignalUser) — this keeps your App ID isolated in one place.
 *
 * SECURITY NOTE: The OneSignal App ID below is meant to be public —
 * it's a client identifier, not a secret. It only lets browsers register
 * for push from YOUR app. Real secrets (OneSignal REST API key, used to
 * SEND notifications) must NEVER appear in this file or any browser code.
 * That key lives only in notify_trigger.py, run on a server, read from
 * an environment variable. See that file's comments for details.
 */

window.addEventListener('load', () => {
  if (typeof OneSignal === 'undefined') {
    console.warn('[KN] OneSignal SDK failed to load — push notifications unavailable this session');
    return;
  }

  OneSignal.init({
    appId: '5cafac8d-0d5d-4d03-816b-483110273e84',
    safari_web_id: '',
    notifyButton: { enable: false },
    allowLocalhostAsSecureOrigin: true,
  }).then(() => {
    console.log('[KN] OneSignal initialized');

    OneSignal.Notifications.addEventListener('permissionChange', (granted) => {
      console.log('[KN] Push permission changed:', granted);
      try {
        const stored = JSON.parse(localStorage.getItem('nk_behaviour') || '{}');
        stored.pushEnabled = !!granted;
        localStorage.setItem('nk_behaviour', JSON.stringify(stored));
      } catch (e) {}
    });
  }).catch((err) => {
    console.error('[KN] OneSignal init failed:', err);
  });
});
