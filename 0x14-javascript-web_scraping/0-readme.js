#!/usr/bin/node

const fs = require('fs');

const path = process.argv[2];

/* const content = 'C is super fun!\n';

fs.writeFile('cisfun', content, (err) => {
  if (err) {
    console.error(err);
  }
}); */

fs.readFile(path, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
