#!/usr/bin/node
const SquareTwo = require('./5-square');

class Square extends SquareTwo {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let col = 0; col < this.width; col++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}

module.exports = Square;
