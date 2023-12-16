with open('./input.txt', 'r') as f:
    d = f.readlines()
    d = [r.strip() for r in d]

# with open('./testinput.txt', 'r') as f:
#     d = f.read().strip()

import re
import itertools
import copy
from functools import cache

t = 0

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

def h(k, l, m):
    if (l[k][0] < 0) or (l[k][1] < 0) or (l[k][0] >= len(morg)) or (l[k][1] >= len(morg[0])) or (l[k][2] in m[l[k][0]][l[k][1]][1]):
        return True
    return False

morg = [[] for _ in range(len(d))]
for i, r in enumerate(d):
    for a in r:
        morg[i].append([a, []])
def tot(l):
    m = copy.deepcopy(morg)

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
            if h(k, l, m): l.pop(k)
            if newb: l.append(newb)
            if len(l):
                if h(len(l) - 1, l, m): l.pop(len(l) - 1)

    u = 0
    for r in m:
        for a in r:
            if a[1]: u += 1
    return u

maxtot = 0
for o in range(len(morg)):
    maxtot = max(tot([[o, 0, "R"]]), maxtot)
    maxtot = max(tot([[o, len(morg[0]) - 1, "L"]]), maxtot)

for p in range(len(morg[0])):
    maxtot = max(tot([[0, p, "D"]]), maxtot)
    maxtot = max(tot([[len(morg) - 1, p, "U"]]), maxtot)

print(maxtot)
