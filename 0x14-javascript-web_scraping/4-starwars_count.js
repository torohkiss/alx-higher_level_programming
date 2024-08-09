#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    let count = 0;
    const data = JSON.parse(body);

    for (const movie of data.results) {
      for (const result of movie.characters) {
        if (result.endsWith('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
