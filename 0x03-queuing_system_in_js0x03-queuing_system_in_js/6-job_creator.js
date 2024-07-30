// Create a job with kue
const kue = require('kue');

const jobData = {
  phoneNumber: '082 539 5632',
  message: 'Data balance: 100GB',
}

const queue = kue.createQueue();

const job = queue.createJob('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log('Notification job created:', job.id);
  }
});

job.on('complete', () => {
    console.log('Notification job completed');
});
job.on('failed', () => {
    console.log('Notification job failed');
});