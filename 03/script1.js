const events = require('events');
const fs = require('fs');
const readline = require('readline');

const symbols = [ '-', '+', '*', '&', '/', '@', '%', '=', '$', '#' ];

(async function processLineByLine() {
    try {
        const rl = readline.createInterface({
            input: fs.createReadStream('input.txt'),
        });

        let total = 0;

        let prevLine = ".";
        rl.on('line', (currentLine) => {
            let number = "";
            let adjacent = false;

            function processChar(line, adjacentLine, i) {
                if (/\d/.test(line[i])) {
                    number += line[i];
                    if (!adjacent && (s(line[Math.max(i - 1, 0)]) || s(line[Math.min(i + 1, line.length)]) || s(adjacentLine[Math.max(i - 1, 0)]) || s(adjacentLine[i]) || s(adjacentLine[Math.min(i + 1, line.length)]))) {
                        adjacent = true;
                    }
                } else if (number) {
                    line = processNumber(line, i);
                }

                return line;
            }

            function processNumber(line, i) {
                if (number) {
                    if (adjacent) {
                        total += Number(number);
                        newLine = line.substring(0, i - number.length);
                        for (let j = 0; j < number.length; j++) {
                            newLine += ".";
                        }
                        newLine += line.substring(i);
                        line = newLine;
                    }
                        
                    number = "";
                    adjacent = false;
                }

                return line;
            }

            for (let i = 0; i < prevLine.length; i++) {
                prevLine = processChar(prevLine, currentLine, i);
            }
            prevLine = processNumber(prevLine, prevLine.length);
            for (let i = 0; i < currentLine.length; i++) {
                currentLine = processChar(currentLine, prevLine, i);
            }
            currentLine = processNumber(currentLine, currentLine.length);

            prevLine = currentLine;
        });

        await events.once(rl, 'close');

        console.log(total);
    } catch (err) {
        console.error(err);
    }
})();

function s(c) {
    return symbols.includes(c);
}
