#!/usr/bin/node

const url = process.argv[2];
const filename = process.argv[3];
const request = require('request');
const fs = require('fs');
request(url, (error, response, body) => {
  if (error) { console.log(error); }
  fs.writeFile(filename, body, 'utf8', (err) => {
    if (err) { console.log(err); }
  });
});
