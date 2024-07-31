// Creates a stock system
const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const listProducts = [
  { "Id": 1, "name": "Suitcase 250", "price": 50, "stock": 4 },
  { "Id": 2, "name": "Suitcase 450", "price": 100, "stock": 10 },
  { "Id": 3, "name": "Suitcase 650", "price": 350, "stock": 2 },
  { "Id": 4, "name": "Suitcase 1050", "price": 550, "stock": 5 }
]

const app = express();

app.listen(1245);

const client = redis.createClient();
client
  .on('connect', () => console.log('Redis client connected.'))
  .on('error', (error) => console.log('Error creating redis client'));

const getPromise = promisify(client.get).bind(client);

/*
  FUNCTIONALITY
*/

/**
 * Gets the item matching the given id, in the listProducts list.
 * @param {number} id the identification number of the item.
 * @returns the item matching the given id, otherwise returns undefined.
 */
function getItemById(id) {
  for (const item of listProducts) {
    if (id === item["Id"]) {
        return item;
    }
  }
  return undefined;
}

/**
 * Reserves an item in the available stock.
 * This is done by storing the item as stock in redis.
 * 
 * @param {number} itemId id of an item.
 * @param {number} stock the total amount for a specific item.
 */
function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

/**
 * Gets the number of reserved stock for a specific item.
 * @param {number} itemId id of an item.
 * @returns the reserved number of stock for a specific type of item.
 */
async function getCurrentReservedStockById(itemId) {
  const stock = await getPromise(`item.${itemId}`);
  if (!stock) {
    return 0;
  }

  return parseInt(stock, 10);
}

/*
  ENDPOINTS
*/

/**
 * Sends the product's information along with its available stock.
 */
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({"status":"Product not found"});
  }

  const reservedStock = await getCurrentReservedStockById(itemId);

  res.json({
    "itemId": item["Id"],
    "itemName": item["name"],
    "price": item["price"],
    "initialAvailableQuantity": item["stock"],
    "currentQuantity": item.stock - reservedStock
  });
});

app.get('/reserve_product/:itemId', async (req,res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({"status":"Product not found"});
  }

  // check if there is enough available stock
  const reservedStock = await getCurrentReservedStockById(itemId);
  if (item.stock - reservedStock <= 0) {
    return res.json({"status":"Not enough stock available", itemId});
  }

  reserveStockById(itemId, reservedStock + 1);
  res.json({"status":"Reservation confirmed","itemId":itemId});
});

app.get('/list_products', (req, res) => {
  let products = [];

  for (const item of listProducts) {
    let object = {
      "itemId": item["Id"],
      "itemName": item["name"],
      "price": item["price"],
      "initialAvailableQuantity": item["stock"]
    };

    products.push(object);
  }

  res.json(products);
});