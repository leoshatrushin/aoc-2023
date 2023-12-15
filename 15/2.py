with open('./input.txt', 'r') as f:
    d = f.read()

import re
import itertools
from functools import cache

t = 0
boxes = [[] for _ in range(256)]

def h(s):
    u = 0
    for a in s:
        u += ord(a)
        u *= 17
        u %= 256
    return u


for s in d.strip().split(','):
    s = re.split('([-=])', s)
    if s[1] == '-':
        boxes[h(s[0])] = list(filter(lambda x: x[0] != s[0], boxes[h(s[0])]))
    if s[1] == '=':
        b = 1
        for i, a in enumerate(boxes[h(s[0])]):
            if a[0] == s[0]:
                boxes[h(s[0])][i] = [s[0], s[2]]
                b = 0
        if b:
            boxes[h(s[0])].append([s[0], s[2]])

for i, b in enumerate(boxes):
    for j, a in enumerate(b):
        t += (i + 1) * (j + 1) * int(a[1])

print(t)
