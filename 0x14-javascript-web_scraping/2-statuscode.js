#!/usr/bin/node
const httpRequest = require('httpRequest');
httpRequest.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
