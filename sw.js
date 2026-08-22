const CACHE_NAME = 'karnata-v2026-fresh-v3';

self.addEventListener('install', (event) => {
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => caches.delete(key))
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  const url = event.request.url;

  // NEVER cache HTML pages, API, Data JSON, or Admin/Officers routes!
  if (
    url.includes('.html') ||
    url.includes('/officers') ||
    url.includes('/admin') ||
    url.includes('/api/') ||
    url.includes('/data/') ||
    url.includes('/districts/') ||
    url.includes('district-notification-engine') ||
    url.includes('/cms') ||
    url.includes('/studio')
  ) {
    // Pass straight to live network without caching
    return;
  }

  // Always fetch live from network
  event.respondWith(
    fetch(event.request, { cache: 'no-store' }).catch(() => caches.match(event.request))
  );
});

self.addEventListener('push', (event) => {
  let data = {
    title: '🚨 ಕರ್ನಾಟಕ ನೈಜ-ಸಮಯ ಅಲರ್ಟ್ — Karnata.in',
    body: 'ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ನೂತನ ಪ್ರಮುಖ ಅಧಿಸೂಚನೆ.',
    icon: '/favicon.ico',
    url: '/officers.html?tab=transfers'
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
    icon: data.icon || '🏛️',
    badge: '🚨',
    vibrate: [200, 100, 200],
    data: { url: data.url || '/officers.html?tab=transfers' }
  };

  event.waitUntil(
    self.registration.showNotification(data.title, options)
  );
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  const urlToOpen = event.notification.data?.url || '/officers.html?tab=transfers';

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
