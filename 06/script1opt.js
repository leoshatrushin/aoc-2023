const fs = require('fs');
const infile = 'input.txt';

let t = 0;

fs.readFileSync(infile, 'utf8').trim().split('\n').forEach(l => {
    let [w, n] = l.split(':')[1].split('|').map(p => p.trim().split(/\s+/));
    t += Math.floor(2 ** (n.filter(n => w.includes(n)).length - 1));
});

console.log(t);
