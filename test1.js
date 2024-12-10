'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}



/*
 * Complete the 'minSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY num
 *  2. INTEGER k
 */


function binaryInsert(num,value){
    let right = num.length -1
    let left = 0
    while (left<=right){
        let mid = Math.floor((right+left)/2)
        if (num[mid] < value) {
            right = mid -1
        }else{
            left = mid +1
        }
    }
    num.splice(left,0,value)
}
function minSum(num, k) {
    // Write your code here
    num.sort((a,b)=>b-a)
    for (let i = 0; i<k ; i++){
        let largest = num.shift()
        let result = Math.ceil(largest/2)
        binaryInsert(num,result)
    }
    return num.reduce((a,b)=>a+b,0)
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const numCount = parseInt(readLine().trim(), 10);

    let num = [];

    for (let i = 0; i < numCount; i++) {
        const numItem = parseInt(readLine().trim(), 10);
        num.push(numItem);
    }

    const k = parseInt(readLine().trim(), 10);

    const result = minSum(num, k);

    ws.write(result + '\n');

    ws.end();
}
