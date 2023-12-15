with open('./input.txt', 'r') as f:
    d = f.readlines()
    d = [r.strip() for r in d]

with open('./input.txt', 'r') as f:
    d = f.read().strip()

import re
import itertools
from functools import cache

t = 0
l = [{} for _ in range(256)]

def h(s):
    u = 0
    for a in s:
        u += ord(a)
        u *= 17
        u %= 256
    return u

for s in d.split(','):
    s = re.split('([-=])', s)
    if s[1] == '-':
        l[h(s[0])].pop(s[0], None)
    if s[1] == '=':
        l[h(s[0])][s[0]] = s[2]

for i, b in enumerate(l):
    for j, a in enumerate(b.values()):
        t += (i + 1) * (j + 1) * int(a)

print(t)
