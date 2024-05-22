#!/usr/bin/node

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

request(url, (error, res, body) => {
  if (error) {
    return console.error(error);
  }
  const characters = JSON.parse(body).characters;
  characters.forEach((char) => {
    request(char, (error, response, body) => {
      if (error) {
        return console.error(error);
      } else {
        console.log(JSON.parse(body).name);
      }
    });
  });
});
