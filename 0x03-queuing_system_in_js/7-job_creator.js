// Track progress and errors with Kue: Create the Job creator

const kue = require("kue");

const jobs = [
  {
    phoneNumber: "4153518780",
    message: "This is the code 1234 to verify your account",
  },
  {
    phoneNumber: "4153518781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4153518743",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4153538781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4153118782",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4153718781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4159518782",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4158718781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4153818782",
    message: "This is the code 4321 to verify your account",
  },
  {
    phoneNumber: "4154318781",
    message: "This is the code 4562 to verify your account",
  },
  {
    phoneNumber: "4151218782",
    message: "This is the code 4321 to verify your account",
  },
];

const queue = kue.createQueue();

for (const job of jobs) {
  const kueJob = queue.create("push_notification_code_2", job).save((err) => {
    if (err) {
      console.log(`error: ${err}`);
    } else {
      console.log(`Notification job created: ${kueJob.id}`);
    }
  });

  kueJob
    .on("progress", (progress) => {
      console.log(`Notification job #${kueJob.id} ${progress}% complete`);
    })
    .on("complete", () => {
      console.log(`Notification job #${kueJob.id} completed`);
    })
    .on("failed", (error) => {
      console.log(`Notification job #${kueJob.id} failed: ${error}`);
    });
}
