const CACHE_NAME = 'karnata-v1-shell';
const SHELL_ASSETS = [
  '/',
  '/index.html',
  '/karnata-theme.css',
  '/data-loader.js',
  '/js/engine/karnata-smart-engine.js'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(SHELL_ASSETS)).catch(() => {})
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(self.clients.claim());
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  // Network-first for freshness, falling back to cache if offline
  event.respondWith(
    fetch(event.request).catch(() => caches.match(event.request))
  );
});

self.addEventListener('push', (event) => {
  let data = {
    title: '🚨 ಕರ್ನಾಟಕ ಮಳೆ ಮುನ್ನೆಚ್ಚರಿಕೆ — KSNDMC Alert',
    body: 'ಉಡುಪಿ, ದಕ್ಷಿಣ ಕನ್ನಡ, ಕೊಡಗು ಮತ್ತು ಮಲೆನಾಡು ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಭಾರೀ ಮಳೆ ಮುನ್ಸೂಚನೆ.',
    icon: '/logo.png',
    url: '/weather.html'
  };

  if (event.data) {
    try {
      data = event.data.json();
    } catch (e) {
      data.body = event.data.text();
    }
  }

  const options = {
    body: data.body,
    icon: data.icon || '🌧️',
    badge: '🚨',
    vibrate: [200, 100, 200],
    data: { url: data.url || '/weather.html' }
  };

  event.waitUntil(
    self.registration.showNotification(data.title, options)
  );
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  const urlToOpen = event.notification.data?.url || '/weather.html';

  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then((clientList) => {
      for (const client of clientList) {
        if (client.url.includes(urlToOpen) && 'focus' in client) {
          return client.focus();
        }
      }
      if (clients.openWindow) {
        return clients.openWindow(urlToOpen);
      }
    })
  );
});
