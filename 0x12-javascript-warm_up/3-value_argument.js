#!/usr/bin/node
const vars = process.argv[2];

if (vars === undefined) {
  console.log('No argument');
} else {
  console.log(vars);
}
