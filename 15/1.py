with open('./input.txt', 'r') as f:
    d = f.read()

import re
import itertools
from functools import cache

t = 0

for s in d.strip().split(','):
    u = 0
    for a in s:
        u += ord(a)
        u *= 17
        u %= 256
    t += u

print(t)
