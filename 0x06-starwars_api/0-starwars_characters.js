#!/usr/bin/node

const req = require('request');

req('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const characters = JSON.parse(body).characters;
  displayInOrder(characters, 0);
});

const displayInOrder = (actors, index) => {
  if (index === actors.length) return;
  req(actors[index], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    displayInOrder(actors, index + 1);
  });
};
