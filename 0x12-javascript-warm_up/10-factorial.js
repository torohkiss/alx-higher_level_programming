#!/usr/bin/node

const ln = parseInt(process.argv[2]);

function factorial (ln) {
  if (ln) {
    if (ln === 0 || ln === 1) {
      return 1;
    } else {
      return ln * factorial(ln - 1);
    }
  } else {
    return 1;
  }
}

console.log(factorial(ln));
