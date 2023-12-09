const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
    input: fs.createReadStream('input.txt'),
});

let firstline = true;
let s = [];
let tmp = [];
let newSeeds = [];

rl.on('line', (l) => {
    if (firstline) {
        firstline = false;
        s = l.split(':')[1].trim().split(/\s+/).map(n => Number(n));
        tmp = [...s];
    }

    if (!l) s = [...tmp];
    if (!/\d/.test(l[0])) return;

    l = l.trim().split(/\s+/).map(n => Number(n));
    newSeeds = s.map(n => {
        if (l[1] <= n && n < l[1] + l[2]) {
            return l[0] + n - l[1];
        } else {
            return n;
        }
    });

    tmp = tmp.map((n, i) => {
        if (newSeeds[i] == s[i]) return n;
        return newSeeds[i];
    })
});

rl.on('close', () => {
    s = [...tmp];
    console.log(Math.min(...s));
});
