// Writes a job creation function

const kue = require("kue");

/**
 * Pushes notifications in the form of a job.
 * @param {Array} jobs an array of objects
 * @param {kue.Queue} queue a kue queue
 */
function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    return new Error('Jobs is not an array');
  }

  for (const object of jobs) {
    const job = queue.create('push_notification_code_3', object)
      .save(() => {
        console.log(`Notification job created: ${job.id}`);
      });

    job
      .on('complete', () => console.log(`Notification job ${job.id} completed`))
      .on('error', (error) => {
        console.log(`Notification job ${job.id} failed: ${error}`);
      })
      .on('progress', (progress, data) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
  }
}

module.exports = createPushNotificationsJobs;