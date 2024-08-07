#!/usr/bin/node

const filePath = process.argv[2];

const fs = require('fs');

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  process.stdout.write(data);
});
