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

const get = promisify(client.GET);
async function displaySchoolValue(schoolName) {
  console.log(await get(schoolName));
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
