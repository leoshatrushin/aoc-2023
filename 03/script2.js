const events = require('events');
const fs = require('fs');
const readline = require('readline');

let total = 0;
let prevprevLine = "";
let prevLine = "";

(async function processLineByLine() {
    try {
        const rl = readline.createInterface({
            input: fs.createReadStream('input.txt'),
        });

        rl.on('line', processLine);

        await events.once(rl, 'close');

        processLine("");

        console.log(total);
    } catch (err) {
        console.error(err);
    }
})();

function processLine(currentLine) {
    for (let i = 0; i < prevLine.length; i++) {
        if (prevLine[i] == "*") {
            let left = getNumberLeft(prevLine, i - 1);
            let right = getNumberRight(prevLine, i + 1);
            let topLeft, topRight, bottomLeft, bottomRight;
            if (0 <= i && i < prevprevLine.length && /\d/.test(prevprevLine[i])) {
                topLeft = getNumber(prevprevLine, i);
                topRight = "";
            } else {
                topLeft = getNumberLeft(prevprevLine, i - 1);
                topRight = getNumberRight(prevprevLine, i + 1);
            }
            if (0 <= i && i < currentLine.length && /\d/.test(currentLine[i])) {
                bottomLeft = getNumber(currentLine, i);
                bottomRight = "";
            } else {
                bottomLeft = getNumberLeft(currentLine, i - 1);
                bottomRight = getNumberRight(currentLine, i + 1);
            }
            if (t(left) + t(right) + t(topLeft) + t(topRight) + t(bottomLeft) + t(bottomRight) == 2) {
                total += n(left) * n(right) * n(topLeft) * n(topRight) * n(bottomLeft) * n(bottomRight);
            }
        }
    }

    prevprevLine = prevLine;
    prevLine = currentLine;
}

function t(str) {
    if (str) {
        return 1;
    }
    return 0;
}

function n(str) {
    if (str) {
        return Number(str);
    }
    return 1;
}

function getNumberLeft(line, i) {
    let number = "";
    for (let j = i; j >= 0; j--) {
        if (/\d/.test(line[j])) {
            number = line[j] + number;
        } else {
            break;
        }
    }
    return number;
}

function getNumberRight(line, i) {
    let number = "";
    for (let j = i; j < line.length; j++) {
        if (/\d/.test(line[j])) {
            number += line[j];
        } else {
            break;
        }
    }
    return number;
}

function getNumber(line, i) {
    let number = "";
    for (let j = i; j >= 0; j--) {
        if (/\d/.test(line[j])) {
            number = line[j] + number;
        } else {
            break;
        }
    }
    for (let j = i + 1; j < line.length; j++) {
        if (/\d/.test(line[j])) {
            number += line[j];
        } else {
            break;
        }
    }
    return number;
}
