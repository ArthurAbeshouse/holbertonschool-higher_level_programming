#!/usr/bin/node

const array = require('./100-data').list;
const mapper = array.map((i, j) => i * j);
console.log(array);
console.log(mapper);
