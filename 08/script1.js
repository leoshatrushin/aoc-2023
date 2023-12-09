const fs = require('fs');
const infile = 'input.txt';

let t = 0;

let contents = fs.readFileSync(infile, 'utf8').trim().split('\n');

let instructions = contents.shift().split('');
contents.shift();

let mapping = new Map();

contents.forEach(l => {
    let [k, v] = l.split('=').map(x => x.trim());
    v = v.split('(')[1].split(')')[0].split(',').map(x => x.trim());
    mapping.set(k, v);
})

let current = "AAA";
let currentInstruction = 0;
while (current != "ZZZ") {
    let v = mapping.get(current);
    if (instructions[currentInstruction++ % instructions.length] == 'L') {
        current = v[0];
    } else {
        current = v[1];
    }
}

console.log(currentInstruction);
