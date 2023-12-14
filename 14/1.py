with open('./input.txt', 'r') as f:
    d = f.readlines()
    d = [r.strip() for r in d]

import re
import itertools
from functools import cache

t = 0

newd = [[] for _ in range(len(d[0]))]
for j, c in enumerate(zip(*d)):
    start = 0
    e = 0
    for i, a in enumerate(c):
        newd[j].append(a)
        if a == 'O':
            e += 1
        if a == '#' or i == len(c) - 1:
            for k in range(start, start + e):
                newd[j][k] = 'O'
            for k in range(start + e, i):
                newd[j][k] = '.'
            if a == 'O' and start + e != len(c):
                newd[j][i] = '.'
            start = i + 1
            e = 0

for i, r in enumerate(newd):
    for j, a in enumerate(r):
        if a == 'O':
            t += len(r) - j

print(t)
