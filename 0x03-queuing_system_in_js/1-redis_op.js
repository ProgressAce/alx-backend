// Node Redis Client and basic operations 

import { createClient, print } from "redis";

const client = createClient();

client
  .on("error", (err) =>
    console.log(`Redis client not connected to the server: ${err}`)
  )
  .on("connect", () => console.log("Redis client connected to the server"));

function setNewSchool(schoolName, value) {
  client.SET(schoolName, String(value), print);
}

function displaySchoolValue(schoolName) {
  console.log(client.GET(schoolName));
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
