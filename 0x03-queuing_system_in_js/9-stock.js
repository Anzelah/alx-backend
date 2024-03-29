const kue = require('kue');

const queue = kue.createQueue();


function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (reply, done) => {
  const { phoneNumber, message } = reply.data;
  sendNotification(phoneNumber, message);
  reply.done();
});
