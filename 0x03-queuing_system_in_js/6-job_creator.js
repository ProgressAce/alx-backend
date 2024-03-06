// Create the Job creator, aka Kue

const kue = require("kue");

const jobData = {
  phoneNumber: "085 267 4823",
  message: "You received a message",
};

const queue = kue.createQueue();
queue
  .on("ready", () => {
    console.info("Queue is ready!");
  })
  .on("error", (err) => console.log(`Error: ${err}`));

const push_notification_code = queue
  .create("push_notification_code", jobData)
  .save((err) => {
    if (err) {
      console.log(`error: ${err}`);
    } else {
      console.log(`Notification job created: ${push_notification_code.id}`);
    }
  });

push_notification_code
  .on("completed", () => {
    console.log("Notification job completed");
  })
  .on("failed", () => {
    console.log("Notification job failed");
  });
