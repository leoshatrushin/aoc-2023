const fs = require('fs');
const infile = 'input.txt';

let t = 1;

let contents = fs.readFileSync(infile, 'utf8').trim().split('\n');

let times = Number(contents.shift().split(":")[1].replace(/\s/g, ''));
let records = Number(contents.shift().split(":")[1].replace(/\s/g, ''));

function custFloor(n) {
    if (Number.isInteger(n)) return n - 1;
    else return Math.floor(n);
}

function custCeil(n) {
    if (Number.isInteger(n)) return n + 1;
    else return Math.ceil(n);
}

let min = custCeil(0.5 * (times - Math.sqrt(times * times - 4 * records)));
let max = custFloor(0.5 * (times + Math.sqrt(times * times - 4 * records)));
t *= max - min + 1;

console.log(t);
