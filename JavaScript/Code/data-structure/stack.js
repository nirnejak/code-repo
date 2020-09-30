class Stack {
  constructor() {
    this.items = []
  }

  push(item) {
    this.items.push(item)
  }

  pop() {
    return this.items.pop()
  }
}

const myStack = new Stack()
myStack.push(10)
console.log(myStack.pop())
console.log(myStack.pop())
