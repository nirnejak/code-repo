numberList = [9, 2, 6, 5];
numberList.sort();
const largest = numberList[numberList.length - 1];

const allDivisible = (numberList, num) => {
    let flag = 0;
    numberList.forEach(n => {
        if (num % n === 0) {
            flag++;
        }
    });
    if (flag === numberList.length) {
        return true;
    } else {
        return false;
    }
}

num = largest;
while (!(allDivisible(numberList, num))) {
    num += largest;
}

console.log(num);