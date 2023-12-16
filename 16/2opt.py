with open('./input.txt', 'r') as f:
    d = f.readlines()
    d = [r.strip() for r in d]

# with open('./testinput.txt', 'r') as f:
#     d = f.read().strip()

import re
import itertools
from functools import cache

t = 0

map = {
    (".", "D"): "D",
    (".", "U"): "U",
    (".", "R"): "R",
    (".", "L"): "L",
    ("/", "D"): "L",
    ("/", "U"): "R",
    ("/", "R"): "U",
    ("/", "L"): "D",
    ("\\", "D"): "R",
    ("\\", "U"): "L",
    ("\\", "R"): "D",
    ("\\", "L"): "U",
    ("|", "D"): "D",
    ("|", "U"): "U",
    ("|", "R"): "U",
    ("|", "L"): "U",
    ("-", "R"): "R",
    ("-", "L"): "L",
    ("-", "D"): "R",
    ("-", "U"): "R"
}

def g(l):
    m = set()
    while l:
        b = tuple(l[0])
        i, j, D = b
        if (i < 0) or (j < 0) or (i >= len(d)) or (j >= len(d[0])) or (b in m):
            l.pop(0)
            continue
        m.add(b)
        if d[i][j] == "|" and D in ["L", "R"]:
            l.append([i + 1, j, "D"])
        if d[i][j] == "-" and D in ["U", "D"]:
            l.append([i, j - 1, "L"])
        D = map[d[i][j], D]
        match D:
            case "R": j += 1
            case "L": j -= 1
            case "U": i -= 1
            case "D": i += 1
        l[0] = [i, j, D]

    u = 0
    m2 = set()
    for (i, j, _) in m:
        if (i, j) in m2: continue
        m2.add((i, j))
        u += 1
    return u

for i in range(len(d)):
    t = max(t, g([[i, 0, "R"]]), g([[i, len(d[0]) - 1, "L"]]))

for j in range(len(d[0])):
    t = max(t, g([[0, j, "D"]]), g([[len(d) - 1, j, "U"]]))

print(t)
