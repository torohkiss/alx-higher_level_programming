#!/usr/bin/node

const ln = parseInt(process.argv[2]);

if (ln) {
  for (let i = 0; i < ln; i++) {
    let row = '';
    for (let j = 0; j < ln; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
