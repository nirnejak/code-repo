class Square {
  constructor(side) {
    this.side = side
    return this
  }

  getArea() {
    return this.side * this.side
  }

  getPerimeter() {
    return 4 * this.side
  }
}

console.log(new Square(10).getArea())
console.log(new Square(20).getArea())