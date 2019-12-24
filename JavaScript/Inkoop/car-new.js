let petrol = 100
let travelled = 0
let stations = []

while (stations.length < 6) {
  let station = generateRandom(100)
  if (!stations.includes(station)) stations.push(station)
}

while (petrol && travelled < 101) {
  let distance = generateRandom(6)
  if ((petrol - distance) > 0) {
    petrol -= distance
    travelled -= distance
  } else {
    travelled = petrol
    petrol = 0
  }

  if (stations.includes(travelled)) {
    petrol += 20
  }
}

function generateRandom(max) {
  return Math.random() * max
}
