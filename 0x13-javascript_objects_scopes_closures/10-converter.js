#!/usr/bin/node

exports.converter = function (base) {
  function conversion (number) {
    return number.toString(base);
  }

  return conversion;
};
