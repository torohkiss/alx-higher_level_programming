#!/usr/bin/node

const url = process.argv[2];

const request = require('request');
/* request(url, function (error, response, body) {
  console.log('code:', response && response.statusCode);
}); */

request
  .get(url)
  .on('response', function (response) {
    console.log('code:', response.statusCode);
  });
