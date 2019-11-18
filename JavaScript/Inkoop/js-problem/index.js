const express = require('express')
const chalk = require('chalk')
const csv = require('csv-parser');
const fs = require('fs');
const cors = require('cors');

const app = express();

app.use(cors())
app.use(express.static('public'))

function fetchCountriesLatLng(filename) {
  return new Promise(function (resolve, reject) {
    let countriesLatLong = {};
    fs.createReadStream(filename)
      .pipe(csv({ headers: false, skipLines: 1 }))
      .on('data', (row) => {
        countriesLatLong[row[3]] = {
          lat: row[1],
          lng: row[2],
        }
      })
      .on('end', () => {
        resolve(countriesLatLong);
      })
  });
}

function fetchCollaborators(filename) {
  return new Promise(function (resolve, reject) {
    let totalNoOfCollaborators = 0;
    let clients = {};
    let index = 0;
    fs.createReadStream(filename)
      .pipe(csv({ separator: ';', headers: false }))
      .on('data', (row) => {
        if (index > 4) {
          let clientCountry = (row[0] || 'Unknown').trim();
          if (!(clientCountry in clients)) {
            clients[clientCountry] = {
              providerCountry: [],
              noOfCollaborations: 0
            }
          }
          clients[clientCountry].providerCountry.push(row[1]);
          clients[clientCountry].noOfCollaborations += parseInt(row[2]);
        } else if (index === 1) {
          totalNoOfCollaborators = parseInt(row[2]);
        }
        index++;
      })
      .on('end', () => {
        resolve({
          clients,
          totalNoOfCollaborators
        })
      })
  });
}

app.get('/data', (req, res) => {
  let fetchCountriesLatLngPromise = fetchCountriesLatLng('country.csv');
  let fetchCollaboratorsPromise = fetchCollaborators('projects-6f2d5e5734d674231d0595233ac12515.csv');

  Promise.all([fetchCountriesLatLngPromise, fetchCollaboratorsPromise]).then(response => {
    const countriesLatLong = response[0];
    const clients = response[1].clients;
    const totalNoOfCollaborators = response[1].totalNoOfCollaborators;
    const totalNoOfClients = Object.keys(clients).length;

    let maxCollaboratedClient = null;
    let minCollaboratedClient = null;
    let maxCountriesClient = null;

    Object.keys(clients).map(key => {
      clients[key].lat = countriesLatLong[key] ? countriesLatLong[key].lat : null;
      clients[key].lng = countriesLatLong[key] ? countriesLatLong[key].lng : null;

      if (minCollaboratedClient === null || minCollaboratedClient.data.noOfCollaborations > clients[key].noOfCollaborations) {
        minCollaboratedClient = {
          name: key,
          data: clients[key]
        };
      };
      if (maxCollaboratedClient === null || maxCollaboratedClient.data.noOfCollaborations < clients[key].noOfCollaborations) {
        maxCollaboratedClient = {
          name: key,
          data: clients[key]
        };
      };

      if (maxCountriesClient === null || maxCountriesClient.data.providerCountry.length < clients[key].providerCountry.length) {
        maxCountriesClient = {
          name: key,
          data: clients[key]
        };
      };
    });

    res.json({
      totalNoOfCollaborators,
      averageCollaborations: totalNoOfCollaborators / totalNoOfClients,
      minCollaboratedClient,
      maxCollaboratedClient,
      maxCountriesClient,
      totalNoOfClients,
      clients
    })
  })
});

const PORT = 3000
app.listen(PORT, () => {
  console.log(chalk.yellow(`🔥  Server started at ${PORT}`))
});
