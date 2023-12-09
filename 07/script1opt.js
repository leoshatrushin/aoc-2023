const fs = require('fs');
const infile = 'input.txt';

let t = 0;

let plays = fs.readFileSync(infile, 'utf8').trim().split('\n').map(l => l.split(" "));

function getCounts(str) {
  const counts = {};
  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    counts[char] = (counts[char] || 0) + 1;
  }
  return Object.values(counts);
}

function getType(hand) {
    let counts = getCounts(hand);
    if (counts.includes(5)) {
        return 6;
    } else if (counts.includes(4)) {
        return 5;
    } else if (counts.includes(3) && counts.includes(2)) {
        return 4;
    } else if (counts.includes(3)) {
        return 3;
    } else if (counts.filter(v => v == 2).length == 2) {
        return 2;
    } else if (counts.includes(2)) {
        return 1;
    }
    return 0;
}

const order = "AKQJT98765432";

function playComparator([a,], [b,]) {
    let aType = getType(a);
    let bType = getType(b);
    if (aType != bType) {
        return aType - bType;
    }
    for (let i in a) {
        if (a[i] != b[i]) {
            return order.indexOf(b[i]) - order.indexOf(a[i]);
        }
    }
}

plays.sort(playComparator).forEach(([, v], i) => {
    t += (i+1) * v;
});

console.log(t);
