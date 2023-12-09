const fs = require('fs');
const infile = 'input.txt';

let t = 0;

function next(s) {
    if (s.length == 1) return 0;
    let diffs = s.map((x, i) => {
        if (i == 0) return 0;
        return x - s[i - 1];
    }).slice(1);
    return s[s.length - 1] + next(diffs);
}

let d = fs.readFileSync(infile, 'utf8').trim().split('\n');
d.forEach(l => {
    l = l.split(' ').map(x => parseInt(x));
    t += next(l);
})

console.log(t);
