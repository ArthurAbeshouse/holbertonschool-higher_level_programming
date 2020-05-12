#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) { console.log(error); }

  const completed = {};
  for (const task of JSON.parse(body)) {
    if (task.completed === true) {
      if (completed[task.userId] in completed) {
	completed[task.userId]++;
      } else { completed[task.userId] = 1; }
    }
  }
  console.log(completed);
});
