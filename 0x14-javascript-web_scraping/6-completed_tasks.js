#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const data = {};
request(url, (error, response, body) => {
  if (error) { console.log(error); }
  const results = JSON.parse(body);
  for (let i = 0; i < results.length; i++) {
    if (results[i].completed === true) {
      if (data[results[i].userId] === undefined) {
        data[results[i].userId] = 1;
      } else {
        data[results[i].userId] += 1;
      }
    }
  }
  console.log(data);
});
