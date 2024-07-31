// Combines Redis, kue and express application
const redis = require('redis');
const kue = require('kue');
const express = require('express');
const { promisify } = require('util');

/*
REDIS CLIENT CONNECT & ASSOCIATED FUNCTIONS
*/

const client = redis.createClient();
client.on('connect', () => console.log('Redis client connected.'));
client.on('error', () => console.log('Error connecting to redis client.'));
const getPromise = promisify(client.get).bind(client);

/**
 * Sets the number of seat available and stores this in redis.
 * @param {number} number the number of available seats
 */
function reserveSeat(number) {
  client.set('available_seats', number);
}

/**
 * Gets the number of available seats.
 * 
 * @returns as an integer, the number of seats that are available.
 */
async function getCurrentAvailableSeats() {
  const seatCount = await getPromise('available_seats')
    .catch((err) => { if (err) return undefined });

  return parseInt(seatCount, 10);
}

// default starting number of available seats
reserveSeat(50);
// should be turned to false when available seats are zero.
let reservationEnabled = true;

/*
KUE QUEUE
*/
const queue = kue.createQueue();

/*
EXPRESS SERVER
*/

const app =  express();
app.listen(1245);

app.get('/available_seats', async (req, res) => {
  const seatCount = await getCurrentAvailableSeats()
    .catch((err) => {
      if (err) {
        return res.json({'error': 'Occured while getting the available seats'});
      }
    });

  res.json({"numberOfAvailableSeats": seatCount});
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ "status": "Reservation are blocked" });
  }

  const reservationJob = queue.createJob('reserve_seat').save((error) => {
    if (error) {
      return res.json({ "status": "Reservation failed" });
    }
  });

  res.json({ "status": "Reservation in process" });

  reservationJob
    .on('complete', () => {
      console.log(`Seat reservation job ${reservationJob.id} completed`);
    })
    .on('failed', (error) => {
      console.log(`Seat reservation job ${reservationJob.id} failed: ${error}`);
    });
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    const seatCount = await getCurrentAvailableSeats()
      .catch((err) => {
        if (err) {
          return res.json({'error': 'Occured while getting the available seats'});
        }
      });

    console.log('/process reservationEnabled check');
    if (!reservationEnabled) {
      return done(new Error('Not enough seats available'));
    } else {
      reserveSeat(seatCount - 1);
      done()
    }

    console.log('/process before seatCount === 0 check');
    if (seatCount - 1 === 0) {
      reservationEnabled = false;
    }
    console.log('/process before res.json');
    res.json({ "status": "Queue processing" });
    done();
  });

});