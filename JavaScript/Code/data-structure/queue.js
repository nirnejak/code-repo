class Queue {
  constructor() {
    this.items = []
  }

  enqueue(item) {
    this.items.push(item)
  }

  dequeue() {
    const item = this.items[0]
    this.items.shift()
    return item
  }
}

const myQueue = new Queue()

myQueue.enqueue(12)
myQueue.enqueue(15)
myQueue.enqueue(18)
myQueue.enqueue(19)
console.log(myQueue.dequeue())
console.log(myQueue.dequeue())
console.log(myQueue.dequeue())