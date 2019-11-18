const chalk = require('chalk')
console.log(chalk.blue.inverse.bold("utils.js running"))

const name = 'Jitendra'
const add = (num1, num2) => num1 + num2;

module.exports = name;
module.exports = add