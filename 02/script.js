const events = require('events');
const fs = require('fs');
const readline = require('readline');

cubeMapping = {
    "red": 12,
    "green": 13,
    "blue": 14
};

(async function processLineByLine() {
    try {
        const rl = readline.createInterface({
            input: fs.createReadStream('/Users/leoshatrushin/dev/2023-advent-of-code/02/input.txt'),
        });

        let total = 0;

        rl.on('line', (line) => {
            let possibleGame = true;
            let gameStart = false;
            let gameID = "";
            let i = 0;
            const minimumCubes = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            game: while (i < line.length) {
                if (!gameStart) {
                    if (/\d/.test(line[i])) {
                        gameID += line[i++];
                        continue;
                    }
                    if (line[i++] == ':') {
                        gameStart = true;
                        continue;
                    }
                }
                i++;
                let count = "";
                while (/\d/.test(line[i])) {
                    count += line[i++];
                }
                i++;
                let color = "";
                while (/\w/.test(line[i])) {
                    if (i == line.length) break;
                    color += line[i++];
                }
                if (minimumCubes[color] < Number(count)) {
                    minimumCubes[color] = Number(count);
                }
                i++;
            }

            total += minimumCubes["red"] * minimumCubes["green"] * minimumCubes["blue"];
        });

        await events.once(rl, 'close');

        console.log(total);
    } catch (err) {
        console.error(err);
    }
})();
