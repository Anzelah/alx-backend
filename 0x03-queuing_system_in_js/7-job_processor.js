const kue = require('kue');

const queue = kue.createQueue();


function sendNotification(phoneNumber, message, job, done) {
  const blacklist = ['4153518780', '4153518781'];
  
  let total = 2;
  let pending = 2;
  
  job.progress(total - pending, total);
  if (blacklist.includes(phoneNumber)) {
    const err = (`Phone number ${phoneNumber} is blacklisted`);
    done(new Error(err));
  } else {
    if (total === pending) {
      console.log(`Sending notification to ${phoneNumber}, with message ${message}`);
    }
  }
}


queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

