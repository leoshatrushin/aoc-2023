with open('./input.txt', 'r') as f:
    d = f.readlines()
    d = [r.strip() for r in d]

import re
import itertools
from functools import cache

t = 0

d = ["".join(["".join(sorted(s, reverse=True)) for s in re.split('(#+)', "".join(c))]) for c in zip(*d)]

for i, r in enumerate(zip(*d)):
    t += r.count('O') * (len(r) - i)

print(t)
