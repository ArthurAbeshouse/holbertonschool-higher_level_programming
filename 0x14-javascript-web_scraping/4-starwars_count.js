#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) { console.log(error); }
  let numOfwedges = 0;
  for (const i of JSON.parse(body).results) {
    for (const j of i.characters) {
      if (j.includes('18')) {
        numOfwedges++;
      }
    }
    console.log(numOfwedges);
  }
});
