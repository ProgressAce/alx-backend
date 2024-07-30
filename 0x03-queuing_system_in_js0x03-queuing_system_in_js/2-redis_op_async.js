// Establishes a redis client connection
import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();
const redisGet = promisify(client.get).bind(client);

client
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', err => {
    console.log('Redis client not connected to the server:', err);
  });

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  await redisGet(schoolName)
  .then((value) => console.log(value))
  .catch((err) => {
    throw err;
  });
}
 
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');