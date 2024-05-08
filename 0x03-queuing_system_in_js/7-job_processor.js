// Track progress and errors with Kue: Create the Job processor

const kue = require("kue");

const blacklistedNums = [4153518780, 4153518781];

function sendNotification(phoneNumber, message, job, done) {
  // track job progress - 0 out of 100
  for (let i = 0; i < 100; i++) {
    if (i === 0) job.progress(0, 100);

    if (blacklistedNums.includes(phoneNumber)) {
      return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    if (i === 50) job.progress(50, 100);
  }

  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

const queue = kue.createQueue();

console.log('Before queue processing');
queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});