#!/usr/bin/node
const file = require('file');
const httpRequest = require('httpRequest');
httpRequest(process.argv[2]).pipe(file.createWriteStream(process.argv[3]));
