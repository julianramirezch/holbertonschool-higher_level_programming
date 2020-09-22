#!/usr/bin/node

const filename = process.argv[2];
const content = process.argv[3];
const fs = require('fs');
fs.writeFile(filename, content, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
