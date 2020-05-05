#!/usr/bin/node
const b = parseInt(process.argv[2]);
if (!isNaN(b)) {
  for (i = 0; i < b; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
