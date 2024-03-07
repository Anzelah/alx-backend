const kue = require('kue');

const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    console.error('Jobs is not an array');
  }
  jobs.forEach((job) => {
    const new_job = queue.create('push_notification_code_3', job).save();

    new_job.on('enqueue', () => {
      console.log(`Notification job created: ${new_job.id}`);
    
    }).on('complete', () => {
      console.log(`Notification job ${new_job.id} completed`);
    
    }).on('failed', (err) => {
      console.log(`Notification job ${new_job.id} failed: ${err}`);
    
    }).on('progress', (progress, data) => {
      console.log(`Notification job #${new_job.id} ${progress}% complete`);
    });
  })
}
