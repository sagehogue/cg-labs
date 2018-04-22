function isDone(string) {
    if (string === 'done') {
        return true;
    } else if (Number.isInteger((parseInt(string))) === true) {
        return parseInt(string);
    }
}

function getSum(array) {
    let numSum = 0;
    let i;
    for (i = 0; i < array.length; i++) {
        numSum += array[i];
    }
    return numSum;
}

function getAverage(aSum, array) {
    return aSum / array.length;
}
let numArray = [];
while (true) {
    input = prompt('Add a number to the array or type \'done\'.').toLowerCase();
    let numOrDone = isDone(input);
    if (numOrDone === true) {
        break
    } else if (typeof numOrDone === "number") {
        numArray.push(numOrDone);
        console.log(numArray);
    } else {
        console.log('Oops. You entered something stupid.')
    }
}
sum = getSum(numArray);
average = getAverage(sum, numArray);
console.log(`${numArray}\nHas a sum value of ${sum} and an average of ${average}`);