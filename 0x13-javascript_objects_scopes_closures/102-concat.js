#!/usr/bin/node

let fs = require('fs');
let fileA = fs.readFileSync(process.argv[2]);
let fileB = fs.readFileSync(process.argv[3]);
fs.writeFileSync(process.argv[4], fileA + fileB);
