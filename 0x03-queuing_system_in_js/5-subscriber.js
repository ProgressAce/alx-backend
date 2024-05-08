// Node Redis client and advanced operations

import { createClient, print } from "redis";

const client = createClient();

client
  .on("connect", () => console.log("Redis client connected to the server"))
  .on("error", (err) =>
    console.log(`Redis client not connected to the server: ${err}`)
  );

client.SUBSCRIBE('holberton school channel', (err) => {
  if (err) console.log(`Error: ${err}`);
});

client.on("message", (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    client.UNSUBSCRIBE('holberton school channel');
    client.quit();
  }
});
