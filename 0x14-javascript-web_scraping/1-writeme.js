#!/usr/bin/node

const data = process.argv[3];

const fs = require('fs');

fs.writeFile('process.argv[2]', data, 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
