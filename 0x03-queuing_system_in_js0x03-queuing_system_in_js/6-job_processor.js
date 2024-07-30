// Processes a job with kue.
const kue = require('kue');

const queue = kue.createQueue();

/**
 * Sends a notification to the phone number and confirms that the job
 * is done.
 * @param {string} phoneNumber the phone number to send the notification to.
 * @param {string} message the message to send the phone number to.
 */
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
