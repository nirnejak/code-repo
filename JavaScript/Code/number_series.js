const numprint = (num) => {
    let printStr = '';

    for(i=1; i <= num; i++) {
        if (i%2 == 0) {
            for(j=0; j<((i*i)-1); j++) {
                printStr+=i;
            }
        }
        else {
            for(j=0; j<(i*i); j++) {
                printStr+=i;
            }
        }
    }
    return printStr;
}

console.log(numprint(5));