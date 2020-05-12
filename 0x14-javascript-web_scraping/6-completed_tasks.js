#!/usr/bin/node

let request = require('request');
let url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  let completed = {};
  for (let task of JSON.parse(body)) {
    if (task.completed === true) {
      if (completed[task.userId]) {
	completed[task.userId]++;
      } else {
	completed[task.userId] = 1;
      }
    }
  }
  console.log(completed);
});
