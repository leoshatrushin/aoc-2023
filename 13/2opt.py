with open('./input.txt', 'r') as f:
    d = f.read().strip().split('\n\n')
    d = [p.split('\n') for p in d]

import re
import itertools
from functools import cache

t = 0

def g(s):
    u = 0
    for i in range(len(s) - 1):
        b = 0
        for j in range(0, i + 1):
            if i + 1 + j >= len(s): break
            b += sum([1 for k in range(len(s[0])) if s[i - j][k] != s[i + 1 + j][k]])
            if b > 1: break
        if b == 1: u += i + 1
    return u

for s in d:
    t += 100 * g(s)
    t += g(tuple(zip(*s)))

print(t)
