const kue = require('kue');

const queue = kue.createQueue();


function sendNotification(phoneNumber, message, job, done) {
  const blacklist = ['4153518780', '4153518781'];
  const total = 100;
  console.log(`Notification job #${job.id} 0% complete`);
 
  if (blacklist.includes(phoneNumber)) {
    const err = (`Phone number ${phoneNumber} is blacklisted`);
    job.failed(new Error(err`Phone number ${phoneNumber} is blacklisted`));
    console.log(`Notification job #${job.id} failed: ${err}`);
  } else {
    for (let processed = 0; processed <= total; processed++) {
      job.progress(processed, total);
      if (processed === 50) {
        console.log(`Notification job #${job.id} 50% complete`);
      }
      console.log(`Sending notification to ${phoneNumber}, with message ${message}`);
    }
  done();
  }
}


queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

