// Node Redis client publisher and subscriber

import { createClient } from "redis";

const publisher = createClient();

publisher
  .on("connect", () => console.log("Redis client connected to the server"))
  .on("error", (err) =>
    console.log(`Redis client not connected to the server: ${err}`)
  );

const sleep = (millisec) =>
  new Promise((resolve) => {
    setTimeout(resolve, millisec);
  });

async function publishMessage(message, time) {
  if (typeof message !== "string" || typeof time !== "number") {
    console.log("TypeError: message should be a string and time a number.");
  }

  await sleep(time);
  console.log(`About to send ${message}`);
  publisher.publish("holberton school channel", message);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
