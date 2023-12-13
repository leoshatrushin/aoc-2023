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
        b = 1
        for j in range(0, i + 1):
            if i + 1 + j >= len(s): break
            if s[i - j] != s[i + 1 + j]: b = 0; break
        if b: u += i + 1
    return u

for s in d:
    t += 100 * g(s)
    t += g(tuple(zip(*s)))

print(t)
