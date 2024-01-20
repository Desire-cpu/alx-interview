#!/usr/bin/node

// Importing 'request' module for making HTTP requests
const httpRequest = require('request');

// Function to retrieve and display the actors in the exact order
const displayActorsInExactOrder = (actorUrls, currentIndex) => {
  // Base case: check if we have processed all actors
  if (currentIndex === actorUrls.length) return;

  // Make a request to get information about the current actor
  httpRequest(actorUrls[currentIndex], function (error, response, responseBody) {
    // Check for errors in the HTTP request
    if (error) throw error;

    // Parse the response body to extract actor information
    const actorInfo = JSON.parse(responseBody);

    // Display the name of the actor
    console.log(actorInfo.name);

    // Recursively call the function for the next actor in the list
    displayActorsInExactOrder(actorUrls, currentIndex + 1);
  });
};

// Main function to start the process
const main = () => {
  // Extracting the film ID from the command line arguments
  const filmId = process.argv[2];

  // Make a request to get information about the film
  httpRequest('https://swapi-api.hbtn.io/api/films/' + filmId, function (error, response, responseBody) {
    // Check for errors in the HTTP request
    if (error) throw error;

    // Parse the response body to extract the list of actors' URLs
    const actorsUrls = JSON.parse(responseBody).characters;

    // Start displaying actors in the exact order
    displayActorsInExactOrder(actorsUrls, 0);
  });
};
