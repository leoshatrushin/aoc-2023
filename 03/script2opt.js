const fs = require('fs');
const readline = require('readline');

const rl = readline.createInterface({
    input: fs.createReadStream('input.txt'),
});

let t = 0;
let l1 = "";
let l2 = "";
const d = c => /\d/.test(c);

function processLine(l1, l2, l3) {
    for (let i = 0; i < l2.length; i++) {
        if (l2[i] == "*") {
            let n = [g(l2, i - 1), g(l2, i + 1)];
            if (d(l1[i])) {
                n.push(g(l1, i));
            } else {
                n.push(g(l1, i - 1), g(l1, i + 1));
            }
            if (d(l3[i])) {
                n.push(g(l3, i));
            } else {
                n.push(g(l3, i - 1), g(l3, i + 1));
            }
            n = n.filter(n => n);
            if (n.length == 2) {
                t += Number(n[0]) * Number(n[1]);
            }

        }
    }
}

function g(l, i) {
    let n = "";
    let j = i;
    while (d(l[j])) n += l[j++];
    if (!n) return "";
    j = i - 1;
    while (d(l[j])) n = l[j--] + n;
    return n;
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
