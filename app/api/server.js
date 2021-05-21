const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

// create express app
const app = express();

// use cors
app.use(cors());

// Setup server port
const port = process.env.PORT || 5000;

// parse requests of content-type - application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }))

// parse requests of content-type - application/json
app.use(bodyParser.json())

// define a root route
app.get('/', (req, res) => {
  res.send("rubri-app api");
});

// Require criteris routes
const criterisRoutes = require('./src/routes/criteris.routes')

// using as middleware
app.use('/api/criteris', criterisRoutes)

// Require nivells routes
const nivellsRoutes = require('./src/routes/nivells.routes')

// using as middleware
app.use('/api/nivells', nivellsRoutes)


// listen for requests
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});