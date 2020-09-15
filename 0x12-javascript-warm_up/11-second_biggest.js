#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2, process.argv.length);
  const arr_copy = [];
  const big = Math.max(...arr);
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== big.toString()) {
      arr_copy.push(arr[i]);
    }
  }
  console.log(Math.max(...arr_copy));
}
