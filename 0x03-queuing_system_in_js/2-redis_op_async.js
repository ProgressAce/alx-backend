// Node Redis Client

import { createClient, print } from "redis";
import { promisify } from "util";

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

const get = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  // gets schoolName key, from Redis DB and logs it to console.
  const value = await get(schoolName).catch((err) => {
    if (err) {
      console.log(`Error displaying: ${err}`);
    }
  });
  console.log(value);
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
