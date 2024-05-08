// Node Redis client publisher and subscriber

import { createClient } from "redis";

const publisher = createClient();

publisher
  .on("connect", () => console.log("Redis client connected to the server"))
  .on("error", (err) =>
    console.log(`Redis client not connected to the server: ${err}`)
  );

function sleep(millisec) {
  return new Promise((resolve) => {
    setTimeout(resolve, millisec);
  });
}

function publishMessage(message, time) {
  sleep(time)
    .then(() => {
      console.log(`About to send ${message}`);
      publisher.PUBLISH('holberton school channel', message);
    });
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);