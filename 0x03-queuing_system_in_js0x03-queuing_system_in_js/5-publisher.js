// Establishes a redis client connection
import { createClient, print } from 'redis';

const client = createClient();
client
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (err) => {
    console.log('Redis client not connected to the server:', err);
  });

/**
 * Publishes a message to the 'holberton school channel' channel after
 * a period of time(in milliseconds).
 * @param {string} message the message to be published
 * @param {number} time amount of time in milliseconds before the message
 *                      is published.
 */
function publishMessage(message, time) {
  setTimeout(function() {
    console.log('About to send', message);
    client.publish('holberton school channel', message);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);