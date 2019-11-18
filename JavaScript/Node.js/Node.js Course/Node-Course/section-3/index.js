const fs = require('fs')
const validator = require('validator')
const chalk = require('chalk')

const firstName = require('./utils')
const getNotes = require('./notes')

console.log(chalk.green.inverse.bold('index.js running'))

fs.writeFileSync('notes.txt', 'Welcome')
fs.appendFileSync('notes.txt', ` ${firstName}`)

console.log(getNotes())
console.log(validator.isEmail('jeetnirnejak@gmail.com'))