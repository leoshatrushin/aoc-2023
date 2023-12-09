const fs = require('fs');
const infile = 'input.txt';

let contents = fs.readFileSync(infile, 'utf-8').trim().split('\n\n');

let s = contents.shift().split(':')[1].trim().split(/\s+/).map(Number);
let tmp = [...s];

contents.forEach(sec => {
    sec.split(':\n')[1].split('\n').forEach(l => {
        l = l.trim().split(/\s+/).map(Number);
        s.forEach((n, i) => {
            if (l[1] <= n && n < l[1] + l[2]) {
                tmp[i] = l[0] + n - l[1];
            }
        })
    });
    s = [...tmp];
})

console.log(Math.min(...s));
