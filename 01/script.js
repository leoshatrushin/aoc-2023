const events = require('events');
const fs = require('fs');
const readline = require('readline');

digitmapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
};

(async function processLineByLine() {
    try {
        const rl = readline.createInterface({
            input: fs.createReadStream('input.txt'),
        });

        let total = 0;
        let firstDigit, lastDigit;
        let firstline = true;
        rl.on('line', (line) => {
            outerloop: for (let i = 0; i < line.length; i++) {
                if (/[\d]/.test(line[i])) {
                    firstDigit = line[i];
                    break;
                }
                for (let key in digitmapping) {
                    if (line.substring(i, i + key.length) === key) {
                        firstDigit = digitmapping[key];
                        break outerloop;
                    }
                }
            }
            firstline = false;
            outerloop: for (let i = line.length - 1; i >= 0; i--) {
                if (/[\d]/.test(line[i])) {
                    lastDigit = line[i];
                    break;
                }
                for (let key in digitmapping) {
                    if (line.substring(i, i + key.length) === key) {
                        lastDigit = digitmapping[key];
                        break outerloop;
                    }
                }
            }
            let number = Number(firstDigit + lastDigit);
            total += number;
        });

        await events.once(rl, 'close');

        console.log(total);
    } catch (err) {
        console.error(err);
    }
})();
