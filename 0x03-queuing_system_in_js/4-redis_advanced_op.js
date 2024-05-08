// Node Redis client and advanced operations

import { createClient, print } from "redis";

const client = createClient();

client
  .on("connect", () => console.log("Redis client connected to the server"))
  .on("error", (err) =>
    console.log(`Redis client not connected to the server: ${err}`)
  );

client.HSET('HolbertonSchools', 'Portland', 50, print);
client.HSET('HolbertonSchools', 'Seattle', 80, print);
client.HSET('HolbertonSchools', 'New York', 20, print);
client.HSET('HolbertonSchools', 'Bogota', 20, print);
client.HSET('HolbertonSchools', 'Cali', 40, print);
client.HSET('HolbertonSchools', 'Paris', 2, print);

client.HGETALL('HolbertonSchools', (err, reply) => {
  if (err) console.log(`Error: ${err}`);

  console.log(reply);
});