#!/usr/bin/node
const file = require('file');
file.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
