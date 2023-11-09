#!/usr/bin/node

const request = require('request');

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// API request and set async for await promise
request(filmURL + filmNum, async function (err, res, body) {
    if (err) return console.error(err);

    // Get the URL of each character in the movie as list object
    const charURLList = JSON.parse(body).characters;

    // make new requests with the URL character list of character pages
    for (const char_URL of charURLList) {
        // await queues requests till they are resolved in other
        await new Promise(function (resolve, reject) {
            request(char_URL, function (err, res, body) {
                if (err) return console.error(err);
                // find the characters and print each
                console.log(JSON.parse(body).name);
            });
        });
    }
});
