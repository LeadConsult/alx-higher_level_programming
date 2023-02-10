#!/usr/bin/node
const httpRequest = require('httpRequest');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
httpRequest(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
