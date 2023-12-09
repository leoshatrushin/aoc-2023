const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
    input: fs.createReadStream('input.txt'),
});

let t = 0;
let l1 = "";
let l2 = "";
let s = c => c && !/\d/.test(c) && c != ".";

function processLine(l1, l2, l3) {
    let n = "";
    for (let i = 0; i < l2.length; i++) {
        while (/\d/.test(l2[i])) n += l2[i++];
        if (n) {
            let a = [l1, l2, l3].some(l => l.slice(Math.max(i - n.length - 1, 0), i + 1).split('').some(s));
            if (a) t += Number(n);
            n = "";
        }
    }
}

rl.on('line', (l) => {
    processLine(l1, l2, l);
    l1 = l2;
    l2 = l;
});

rl.on('close', () => {
    processLine(l1, l2, "");
    console.log(t);
});
