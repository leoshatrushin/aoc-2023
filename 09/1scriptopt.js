const fs = require('fs');
const infile = 'input.txt';

let t = 0;

function n(s) {
    if (!s.length) return 0;
    let d = s.map((x, i) => x - s[i - 1]).slice(1);
    return s.pop() + n(d);
}

let d = fs.readFileSync(infile, 'utf8').trim().split('\n');
d.forEach(l => {
    l = l.split(' ').map(x => parseInt(x));
    t += n(l);
})

console.log(t);
