#!/usr/bin/node
// prints characters of starwars movies one after the other

const axios = require('axios');

async function getMovieCharacters(movieId) {
  try {
    const response = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
    const movieData = response.data;
    
    if (!movieData.characters || movieData.characters.length === 0) {
      console.log(`No characters found for the given movie ID: ${movieId}`);
      process.exit(1);
    }

    return movieData.characters;
  } catch (error) {
    console.error(`Error fetching movie details: ${error.message}`);
    process.exit(1);
  }
}

async function getCharacterName(characterUrl) {
  try {
    const response = await axios.get(characterUrl);
    const characterData = response.data;
    return characterData.name || 'Unknown';
  } catch (error) {
    console.error(`Error fetching character details: ${error.message}`);
    process.exit(1);
  }
}

async function main() {
  if (process.argv.length !== 3) {
    console.log('Usage: node 0-starwars_characters.js <movie_id>');
    process.exit(1);
  }

  const movieId = process.argv[2];
  const characters = await getMovieCharacters(movieId);

  console.log(`Characters for Movie ${movieId}:`);

  for (const characterUrl of characters) {
    const characterName = await getCharacterName(characterUrl);
    console.log(characterName);
  }
}

main();
