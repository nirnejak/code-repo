function* name() {
  const x = 7;
  yield x;
}


function* get3() {
  let x = 0;
  yield x;

  x += 1
  yield x;

  x += 1
  yield x
}

const gen = get3()
const v1 = get.next()
const v2 = get.next()
const v3 = get.next()


for (let v in get3()) {
  console.log(v)
}