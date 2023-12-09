const events = require('events');
const fs = require('fs');
const readline = require('readline');

(async function processLineByLine() {
    try {
        const rl = readline.createInterface({
            input: fs.createReadStream('input.txt'),
        });

        let total = 0;
        let cardMatches = [];
        let numCards = [];

        rl.on('line', (line) => {
            let winningNumbers = new Set();
            let readingWinningNumbers = false;
            let readingNumbers = false;
            let number = "";
            let ticketTotal = 0;
            for (let i = 0; i < line.length; i++) {
                if (!readingWinningNumbers && line[i] === ':') {
                    readingWinningNumbers = true;
                    continue;
                }

                if (readingWinningNumbers && line[i] == " ") {
                    if (number) winningNumbers.add(Number(number));
                    number = "";
                } else if (readingWinningNumbers) {
                    number += line[i];
                }

                if (readingWinningNumbers && line[i] === '|') {
                    readingWinningNumbers = false;
                    readingNumbers = true;
                    continue;
                }

                if (readingNumbers && line[i] === ' ') {
                    if (number) {
                        if (winningNumbers.has(Number(number))) {
                            ticketTotal++;
                        }
                    }
                    number = "";
                } else if (readingNumbers) {
                    number += line[i];
                }

                if (readingNumbers && i === line.length - 1) {
                    if (number) {
                        if (winningNumbers.has(Number(number))) {
                            ticketTotal++;
                        }
                    }
                }
            }

            cardMatches.push(ticketTotal);
            numCards.push(1);
        });

        await events.once(rl, 'close');

        for (let i = 0; i < numCards.length; i++) {
            total += numCards[i];
            for (let j = i + 1; j < i + 1 + cardMatches[i]; j++) {
                numCards[j] += numCards[i];
            }
        }

        console.log(total);
    } catch (err) {
        console.error(err);
    }
})();
