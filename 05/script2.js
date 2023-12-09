const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
    input: fs.createReadStream('input.txt'),
});

let firstline = true;
let s = [];
let rangeMap = new Map();
rangeMap.set(0, 0);
let newRangeMap = new Map();
newRangeMap.set(0, 0);

rl.on('line', (l) => {
    if (firstline) {
        firstline = false;
        s = l.split(':')[1].trim().split(/\s+/).map(n => Number(n));
    }

    if (!l) onSectionEnd();
    if (!/\d/.test(l[0])) return;

    l = l.trim().split(/\s+/).map(n => Number(n));
    newRangeMap.set(l[1], l[0]);
    if (!newRangeMap.has(l[1] + l[2])) {
        newRangeMap.set(l[1] + l[2], l[1] + l[2]);
    }
});

function onSectionEnd() {
    rangeMap = combineMaps();
    newRangeMap = new Map();
    newRangeMap.set(0, 0);
}

function combineMaps() {
    let combinedMap = new Map();
    for (let [k, v] of rangeMap) {
        let e = findKey(newRangeMap, v);
        combinedMap.set(k, e[1] + v - e[0]);
    }
    for (let [k, v] of newRangeMap) {
        let e = findValue(rangeMap, k);
        combinedMap.set(e[0] + k - e[1], v);
    }
    return combinedMap;
}

function findKey(m, target) {
    let candidateKey = -1;
    let candidateValue = -1;
    for (let [k, v] of m) {
        if (k <= target && k > candidateKey) {
            candidateKey = k;
            candidateValue = v;
        }
    }
    return [candidateKey, candidateValue];
}

function findValue(m, target) {
    let candidateKey = -1;
    let candidateValue = -1;
    for (let [k, v] of m) {
        if (v <= target && v > candidateValue) {
            candidateKey = k;
            candidateValue = v
        }
    }
    return [candidateKey, candidateValue];
}

rl.on('close', () => {
    onSectionEnd();
    let minimum = Infinity;
    for (let i = 0; i < s.length; i++) {
        let lowerEntry = findKey(rangeMap, s[i]);
        minimum = Math.min(minimum, lowerEntry[1] + s[i] - lowerEntry[0]);
        for (let [k, v] of rangeMap) {
            if (k >= s[i] && k <= s[i] + s[i+1]) {
                minimum = Math.min(minimum, v);
            }
        }
        i++;
    }
    console.log(minimum);
});
