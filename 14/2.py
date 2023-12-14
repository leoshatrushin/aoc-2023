with open('./input.txt', 'r') as f:
    d = f.readlines()
    d = [r.strip() for r in d]

import re
import itertools
from functools import cache

t = 0

@cache
def g(d):
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
    for r in newd:
        r.reverse()
    return tuple([tuple(r) for r in newd])

d = tuple(d)
mem = {}
domem = True
l = 0
while l < 1000000000:
    res = g(g(g(g(d))))
    if res in mem:
        period = l - mem[res]
        periodsleft = (1000000000 - l - 1) // period
        l += periodsleft * period
        mem = {}
        domem = False
    if domem: mem[res] = l
    l += 1
    d = res

for j, c in enumerate(zip(*d)):
    for i, a in enumerate(c):
        if a == 'O':
            t += len(c) - i

print(t)
