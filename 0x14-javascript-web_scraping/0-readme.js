#!/usr/bin/node

const arg = process.argv[2];
const fs = require('fs');
fs.readFile(arg, 'utf8', function (err, data) {
  if (data) {
    console.log(data);
  } else {
    console.log(err);
  }
});
