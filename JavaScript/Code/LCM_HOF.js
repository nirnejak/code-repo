let lcm, nums = [2, 4, 9]
for (lcm = Math.max(...nums); !nums.every(n => lcm % n === 0); lcm += Math.max(...nums));

console.log(lcm)
