with open('./input.txt', 'r') as f:
    d = f.readlines()
    d = [r.strip() for r in d]

# with open('./testinput.txt', 'r') as f:
#     d = f.read().strip()

import re
import itertools
from functools import cache

t = 0

m = [[] for _ in range(len(d))]
l = [[0, 0, "R"]]

for i, r in enumerate(d):
    for a in r:
        m[i].append([a, []])

def g(i, j, d):
    match d:
        case "R": return i, j+1
        case "L": return i, j-1
        case "U": return i-1, j
        case "D": return i+1, j
    return i, j

slashmap = {
    "D": "L",
    "U": "R",
    "R": "U",
    "L": "D"
}

backslashmap = {
    "D": "R",
    "U": "L",
    "R": "D",
    "L": "U"
}

def h(k):
    if (l[k][0] < 0) or (l[k][1] < 0) or (l[k][0] >= len(m)) or (l[k][1] >= len(m[0])) or (l[k][2] in m[l[k][0]][l[k][1]][1]):
        l.pop(k)

while l:
    for k, b in enumerate(l):
        i, j, d = b
        m[i][j][1].append(d)
        newb = 0
        match m[i][j][0]:
            case ".": l[k][0], l[k][1] = g(i, j, d)
            case "/": l[k][0], l[k][1] = g(i, j, slashmap[d]); l[k][2] = slashmap[d]
            case "\\": l[k][0], l[k][1] = g(i, j, backslashmap[d]); l[k][2] = backslashmap[d]
            case "|":
                if d in ["U", "D"]: l[k][0], l[k][1] = g(i, j, d)
                else: l[k][0], l[k][1] = g(i, j, slashmap[d]); l[k][2] = slashmap[d]; newb = list(g(i, j, backslashmap[d])) + [backslashmap[d]]
            case "-":
                if d in ["L", "R"]: l[k][0], l[k][1] = g(i, j, d)
                else: l[k][0], l[k][1] = g(i, j, slashmap[d]); l[k][2] = slashmap[d]; newb = list(g(i, j, backslashmap[d])) + [backslashmap[d]]
        h(k)
        if newb: l.append(newb)
        h(len(l) - 1)

for r in m:
    for a in r:
        if a[1]: t += 1

print(t)
