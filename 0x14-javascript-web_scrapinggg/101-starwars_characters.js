#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

request(url, (err, res, body) => {
  if (err) {
    return console.error(err);
  }
  const index = 0;
  const characters = JSON.parse(body).characters;
  printCharcter(characters, index);
});

const printChar = (url, i) => {
  request(url[i], (err, res, body) => {
    if (err) {
      return console.error(err);
    }
    console.log(JSON.parse(body).name);
    if (++i < url.length) {
      printChar(url, i++);
    }
  });
};
