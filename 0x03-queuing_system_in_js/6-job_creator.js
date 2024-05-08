// Create the Job creator, aka Kue

const kue = require('kue');

const queue = kue.createQueue();
queue
  .on('ready', () => console.info('Queue is ready.'))
  .on('error', (err) => console.log(`Queue error: ${err}`));

const jobData = {
  phoneNumber: "078 297 0495",
  message: "You have received Discord message.",
}

const job = queue.create('push_notification_code', jobData)
  .save((err) => {
  if (err) {
    console.log(`Job error: ${err}`);
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});

job
  .on("complete", () => console.log('Notification job completed'))
  .on('failed', () => console.log('Notification job failed'));