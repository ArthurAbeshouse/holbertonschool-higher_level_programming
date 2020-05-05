#!/usr/bin/node
const b = parseInt(process.argv[2]);
if (isNaN(b)) {
  console.log('Missing size');
} else {
  for (i = 0; i < b; i++) {
    console.log('X'.repeat(b));
  }
}
