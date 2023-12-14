with open('./input.txt', 'r') as f:
    d = f.readlines()
    d = [r.strip() for r in d]

import re
import itertools
from functools import cache

t = 0

def g(d):
    return tuple(["".join(["".join(sorted(s, reverse=True)) for s in re.split('(#+)', "".join(c))])[::-1] for c in zip(*d)])

m = {}
i = 0
while i < 1000000000:
    d = g(g(g(g(d))))
    if d in m:
        T = i - m[d]
        Trem = (1000000000 - 1 - i) // T
        i += Trem * T
    m[d] = i
    i += 1

for i, r in enumerate(d):
    t += r.count('O') * (len(d) - i)

print(t)
