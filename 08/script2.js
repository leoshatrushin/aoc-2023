const fs = require('fs');
const infile = 'input.txt';

let contents = fs.readFileSync(infile, 'utf8').trim().split('\n');

let instructions = contents.shift().split('');
contents.shift();

let nodes = [];
let aNodes = [];
let mapping = new Map();

contents.forEach(l => {
    let [k, v] = l.split('=').map(x => x.trim());
    v = v.split('(')[1].split(')')[0].split(',').map(x => x.trim());
    mapping.set(k, v);
    nodes.push(k);
    if (k[k.length - 1] == 'A') {
        aNodes.push(k);
    }
})

let loopNodes = [];
let loopStarts = [];
let loopLengths = [];
let offsets = [];

aNodes.forEach((k, i) => {
    let memory = new Map();
    let currentInstruction = 0;
    let node = k;
    while (true) {
        do {
            let v = mapping.get(node);
            if (instructions[currentInstruction++ % instructions.length] == 'L') {
                node = v[0];
            } else {
                node = v[1];
            }
        } while (node[node.length - 1] != 'Z');
        if (memory.has(node + ":" + (currentInstruction % instructions.length))) {
            break;
        }
        memory.set(node + ":" + (currentInstruction % instructions.length), currentInstruction);
    }
    loopNodes.push([node, currentInstruction % instructions.length]);
    loopStarts.push(memory.get(node + ":" + (currentInstruction % instructions.length)));
    loopLengths.push(currentInstruction - loopStarts[i]);
    offsets.push([]);
    for (let [_, v] of memory) {
        if (loopStarts[loopStarts.length - 1] < v) {
            offsets[i].push(v - loopStarts[i]);
        }
    }
});

console.log(loopNodes);
console.log(loopStarts);
console.log(loopLengths);
console.log(offsets);

// find lcm of loopLengths
let lcm = loopLengths[0];
for (let i = 1; i < loopLengths.length; i++) {
    let b = loopLengths[i];
    let a = lcm;
    while (a != b) {
        if (a > b) {
            a -= b;
        } else {
            b -= a;
        }
    }
    lcm = lcm * loopLengths[i] / a;
}
console.log(lcm);
