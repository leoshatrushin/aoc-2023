const fs = require('fs');
const infile = 'input.txt';

let t = 0;
let counts = [];
let matches = [];

fs.readFileSync(infile, 'utf8').trim().split('\n').forEach(l => {
    let [w, n] = l.split(':')[1].split('|').map(p => p.trim().split(/\s+/));
    counts.push(1);
    matches.push(n.filter(n => w.includes(n)).length);
});

for (let i = 0; i < counts.length; i++) {
    t += counts[i];
    for (let j = i + 1; j < i + 1 + matches[i]; j++) {
        counts[j] += counts[i];
    }
}

console.log(t);
