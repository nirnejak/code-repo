class Notes {
  constructor(name) {
    this.name = name
    this.fs = require('fs')
    this.fs.writeFileSync(`${this.name}.txt`)
  }
  addNote(note) {
    this.fs.appendFileSync(`${this.name}.txt`, note)
  }
  getNotes(note) {
    this.fs.appendFileSync(`${this.name}.txt`, note)
  }
}