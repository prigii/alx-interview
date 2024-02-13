#!/usr/bin/node
// Display one character name per line in the same
// order as the “characters” list in the /films/ endpoint

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const filmData = JSON.parse(body);
    const characters = filmData.characters;
    const characterRequests = characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, function (error, response, body) {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          } else {
            reject(`Error: Failed to fetch character data for ${characterUrl}`);
          }
        });
      });
    });
    Promise.all(characterRequests)
      .then(characterNames => {
        characterNames.forEach(name => {
          console.log(name);
        });
      })
      .catch(error => {
        console.error('Error:', error);
      });
  } else {
    console.error('Failed to fetch film data:', error);
  }
});
