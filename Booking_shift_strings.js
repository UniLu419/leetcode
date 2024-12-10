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
 * Complete the 'getShiftedString' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. STRING s
 *  2. INTEGER leftShifts
 *  3. INTEGER rightShifts
 */

function getShiftedString(s, leftShifts, rightShifts) {
    // Write your code here
    const sLeng = s.length;
    let shiftLength = (leftShifts - rightShifts)% sLeng;
    if (shiftLength < 0){
        shiftLength += sLeng;
    }
    return s.slice(shiftLength)+s.slice(0,shiftLength)
}
function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    const leftShifts = parseInt(readLine().trim(), 10);

    const rightShifts = parseInt(readLine().trim(), 10);

    const result = getShiftedString(s, leftShifts, rightShifts);

    ws.write(result + '\n');

    ws.end();
}
