#!/usr/bin/node

exports.converter = function (base) {
  const conversion = (number) => {
    return number.toString(base);
  };

  return conversion;
};
