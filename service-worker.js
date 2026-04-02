self.addEventListener('push', event => {
  const options = { body: event.data.text(), icon: 'icon-192.png' };
  event.waitUntil(self.registration.showNotification('Recordatorio Escolar', options));
});