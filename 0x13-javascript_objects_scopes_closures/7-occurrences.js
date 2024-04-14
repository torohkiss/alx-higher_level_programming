#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count;

  for (let i = 0; i < list.length; i++) {
    count = list.filter(a => a === searchElement).length;
  }
  return count;
};
