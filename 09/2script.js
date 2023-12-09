const fs = require('fs');
const infile = 'input.txt';

let t = 0;

let d = fs.readFileSync(infile, 'utf8').trim().split('\n');
d.forEach(l => {
    l = l.split(' ').map(x => parseInt(x));
    let diffs = [[...l]];
    while (!diffs[diffs.length - 1].every(x => x == 0)) {
        diffs.push(diffs[diffs.length - 1].map((x, i) => {
            if (i == 0) return 0;
            return x - diffs[diffs.length - 1][i - 1];
        }).slice(1));
    }
    let val = 0;
    for (let i = diffs.length - 1; i >= 0; i--) {
        val = diffs[i][0] - val;
    }
    t += val;
})

console.log(t);
