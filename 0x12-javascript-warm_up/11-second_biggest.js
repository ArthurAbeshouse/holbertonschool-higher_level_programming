#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const lowHi = process.argv.slice(2).sort((a, b) => b - a);
  console.log(lowHi[1]);
}
