#!/usr/bin/node

const num = process.argv[2];
if (!isNaN(parseInt(num, 10))) {
  console.log('My number: ' + parseInt(num, 10));
} else {
  console.log('Not a number');
}
