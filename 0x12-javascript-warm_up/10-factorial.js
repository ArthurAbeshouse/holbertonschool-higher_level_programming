#!/usr/bin/node
function factorial (i) {
  if (i === 0 || isNaN(i) || i < 2) {
    return 1;
  } else {
    return i * factorial(i - 1);
  }
}
console.log(factorial(process.argv[2]));
