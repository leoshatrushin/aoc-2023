const fs = require('fs');
const infile = 'input.txt';

let t = 0;

let contents = fs.readFileSync(infile, 'utf8').trim().split('\n');
let plays = {};

function hasTwoPairs(values) {
    let pairs = 0;
    for (const value of values) {
        if (value == 2) {
            pairs++;
        }
    }
    return pairs === 2;
}

function getCharacterCount(str) {
  const count = {};

  for (let i = 0; i < str.length; i++) {
    const char = str[i];
    count[char] = (count[char] || 0) + 1;
  }

  return count;
}

function getType(hand) {
    let type = 0;
    let handWOJ = hand.split("").filter(c => c != "J").join("");
    let numJ = hand.length - handWOJ.length;
    let counts = getCharacterCount(handWOJ);
    let values = Object.values(counts);
    if (values.length == 0) {
        values = [5];
    } else {
        let maxVal = Math.max(...values);
        for (let i = 0; i < values.length; i++) {
            if (values[i] == maxVal) {
                values[i] += numJ;
                break;
            }
        }
    }
    if (values.includes(5)) {
        type = 6;
    } else if (values.includes(4)) {
        type = 5;
    } else if (values.includes(3) && values.includes(2)) {
        type = 4;
    } else if (values.includes(3)) {
        type = 3;
    } else if (hasTwoPairs(values)) {
        type = 2;
    } else if (values.includes(2)) {
        type = 1;
    }
    return type;
}

contents.forEach(l => {
    l = l.split(" ");
    plays[l[0]] = l[1];
})

function sortObjectByKeys(obj, comparator) {
  // Get the keys of the object and sort them with the custom comparator
  const sortedKeys = Object.keys(obj).sort(comparator);

  // Map the sorted keys to their corresponding values
  const sortedValues = sortedKeys.map(key => obj[key]);

  return sortedValues;
}

const order = "AKQT98765432J";

// Custom comparator function example (ascending, case-insensitive)
function customComparator(a, b) {
    let aRank = getType(a);
    let bRank = getType(b);
    if (aRank != bRank) {
        return aRank - bRank;
    } else {
        for (let i = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                return order.indexOf(b[i]) - order.indexOf(a[i]);
            }
        }
    }
    return 0;
}

sortObjectByKeys(plays, customComparator).forEach((p, i) => {
    t += (i+1) * p;
});

console.log(t);
