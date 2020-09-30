class Tree {
  constructor(data) {
    this.data = data || null
    this.left = null
    this.right = null
  }

  insert(data) {
    if (this.data) {
      this.left = new Tree(data)
    } else {
      this.data = null
    }
  }
}

const myTree = new Tree()
myTree.insert(12)
myTree.insert(12)