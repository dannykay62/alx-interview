#!/usr/bin/node

const request = require('request');

const movie_Num = process.argv[2] + '/';
const movie_URL = 'https://swapi-api.hbtn.io/api/films/';

// API request and set async for await promise
request(movie_URL + movie_Num, async function (err, res, body) {
  if (err) return console.error(err);

  // Get the URL of each character in the movie as list object
  const charURLList = JSON.parse(body).characters;

  // make new requests with the URL character list of character pages
  for (const charURL of charURLList) {
    // await queues requests till they are resolved in other
    await new Promise(function (resolve, reject) {
      request(charURL, function (err, res, body) {
        if (err) return console.error(err);

        // find the characters and print each
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});