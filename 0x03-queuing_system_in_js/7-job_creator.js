// Track progress and errors with Kue: Create the Job creator
const kue = require("kue");

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

const queue = kue.createQueue();

// create jobs and push to queue
for (const job of jobs) {
  const pushNoteJob = queue.createJob('push_notification_code_2', job);
  pushNoteJob.save((err) => {
    if (err) {
      console.log(`Job creation error: ${err}`);
    } else {
      console.log(`Notification job created: ${pushNoteJob.id}`);
    }
  });

  pushNoteJob
    .on('progress', (progress) =>
      console.log(`Notification job ${pushNoteJob.id} ${progress}% complete`)
    )
    .on('complete', (result) =>
      console.log(`Notification job ${pushNoteJob.id} completed`))
    .on('failed', (error) => 
      console.log(`Notification job ${pushNoteJob.id} failed: ${error}`)); 
}