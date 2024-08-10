#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileToWrite = process.argv[3];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(fileToWrite, body, 'utf8', () => {});
  }
});
