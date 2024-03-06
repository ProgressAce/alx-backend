// Track progress and errors with Kue: Create the Job processor

const kue = require("kue");

const blacklistedNumbers = ["4153518780", "4153518781"];

function sendNotification(phoneNumber, message, job, done) {
  for (let x = 0; x <= 100; x++) {
    if (x === 0) {
      job.progress(0, 100);
    }
    if (blacklistedNumbers.includes(phoneNumber)) {
      return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }

    if (x === 50) {
      job.progress(50, 100);
      console.log(
        `Sending notification to ${phoneNumber}, with message: ${message}`
      );
    }
  }
  done();
}

const queue = kue.createQueue();

queue.process("push_notification_code_2", 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
