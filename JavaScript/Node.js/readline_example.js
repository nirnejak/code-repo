const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const fact = (num) => {
	let factorial = 1
	for(let i=1; i<=num; i++){
		factorial *= i;
	}
	return factorial;
}

rl.question('Enter a number to calculate it\'s Factorial : ', (num) => {
  answer = fact(num);
  console.log(`Factorial of ${num} is ${answer}`);
  rl.close();
});
