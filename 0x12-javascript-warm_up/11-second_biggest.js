#!/usr/bin/node

const ln = process.argv.length;

if (ln < 3) {
  console.log(0);
} else if (ln === 3) {
  console.log(0);
} else {
  process.argv.sort();
  const i = process.argv[ln - 2];
  console.log(i);
}
