#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    supers(size, size);
    this.size = size;
  }
}

module.extends = Square;
