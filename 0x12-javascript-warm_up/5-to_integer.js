#!/usr/bin/node

let num = parseInt(process.argv[2]);

if (num) {
  console.log('My number: ' + math.floor(num));
} else {
  console.log('Not a number');
}
