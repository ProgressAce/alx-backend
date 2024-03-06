// Node Redis Client

import { createClient, print } from "redis";

const client = createClient();

client
  .on("error", (err) =>
    console.log(`Redis client not connected to the server: ${err}`)
  )
  .on("connect", () => console.log("Redis client connected to the server"));

function setNewSchool(schoolName, value) {
  // sets a value for the schoolName key, in Redis.
  client.set(schoolName, String(value), print);
}

function displaySchoolValue(schoolName) {
  // gets schoolName key, from Redis DB and logs it to console.
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log(`Error displaying: ${err}`);
    } else {
      console.log(reply);
    }
  });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
