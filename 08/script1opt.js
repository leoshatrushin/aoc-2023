const fs = require('fs');
const infile = 'input.txt';

let contents = fs.readFileSync(infile, 'utf8').trim().split('\n');

let instructions = contents.shift().split('');
contents.shift();

let map = new Map();

contents.forEach(l => {
    let [k, v] = l.split('=').map(x => x.trim());
    v = v.slice(1, -1).split(',').map(x => x.trim());
    map.set(k, v);
})

let k = "AAA";
let i = 0;
while (k != "ZZZ") {
    let v = map.get(k);
    if (instructions[i++ % instructions.length] == 'L') {
        k = v[0];
    } else {
        k = v[1];
    }
}

console.log(i);
