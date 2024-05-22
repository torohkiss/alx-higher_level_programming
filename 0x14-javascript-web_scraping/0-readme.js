#!/usr/bin/node

const filePath = process.argv[2];

const fs = require('fs');

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('Error reading file:', err);
    return;
  }
  console.log('File contents:', data);
});
