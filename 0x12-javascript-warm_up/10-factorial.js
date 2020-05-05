#!/usr/bin/node
function factorial (i) {
  if (i === 0 || isNaN(i) || i <= 1) {
    return 1;  
  }
  return (i * factorial(i - 1));
}
console.log(factorial(process.argv[2]));
