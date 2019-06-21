function myMap(arr, func) => {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        result.push(func(arr[i]));
    }
    return result;
}
function myFilter(arr, func) => {
    let result = [];
    for (let i = 0; i < arr.length; i++) {
        if (func(arr[i])) {
            result.push(arr[i])
        }
    }
    return result;
}


let testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
myMap(testArray, x => x * x);
myFilter(testArray, x => x % 2 ? false : true);