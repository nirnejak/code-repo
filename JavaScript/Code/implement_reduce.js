const nums = [1, 2, 3, 4, 57]

// console.log(nums.reduce((acc, value) => acc + value))

nums.myreduce = function (func) {
  let accumulator = 0
  for (let i = 0; i < this.length; i++)
    accumulator = func(accumulator, this[i], i, this);
  return accumulator;
}

console.log(nums.myreduce((acc, value) => acc + value))
