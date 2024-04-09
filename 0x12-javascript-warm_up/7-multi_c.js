#!/usr/bin/node

const ln = parseInt(process.argv[2]);

if (ln) {
  for (let i = 0; i < ln; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
