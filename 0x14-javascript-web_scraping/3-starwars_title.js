#!/usr/bin/node

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');
request(url, (error, response, body) => {
  if (error) { console.log(error); }
  console.log(JSON.parse(body).title);
});
