#!/usr/bin/node
const vars = process.argv.length;

if (vars <= 2) {
  console.log('No argument');
} else if (vars === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
