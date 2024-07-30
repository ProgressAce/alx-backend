// Uses kue to processes multiple jobs
const kue = require('kue');

const blacklistedNumbers = [4153518780, 4153518781];

/**
 * Sends a notification to the phone number and confirms that the job
 * is done.
 * @param {number} phoneNumber the phone number to send to.
 * @param {string} message the message to give to phone number
 * @param {kue.Job} job 
 * @param {import('kue').DoneCallback} done indicates the job's completion.
 * @returns 
 */
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

const queue = kue.createQueue();
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(parseInt(phoneNumber, 10), message, job, done);
});
