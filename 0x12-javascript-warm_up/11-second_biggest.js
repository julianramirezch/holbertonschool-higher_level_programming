#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2, process.argv.length);
  const arrCopy = [];
  const big = Math.max(...arr);
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== big.toString()) {
      arrCopy.push(arr[i]);
    }
  }
  console.log(Math.max(...arrCopy));
}
