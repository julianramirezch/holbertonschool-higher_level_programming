#!/usr/bin/node

const url = process.argv[2];
let cont = 0;
const request = require('request');

request(url, (error, response, body) => {
  if (error) { console.log(error); }
  const films = JSON.parse(body).results;
  for (let i = 0; i < films.length; i++) {
    const chars = films[i].characters;
    for (let j = 0; j < chars.length; j++) {
      if (chars[j].includes('18')) {
        cont++;
      }
    }
  }
  console.log(cont);
});
