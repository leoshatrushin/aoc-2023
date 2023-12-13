import re
import itertools
from functools import cache

with open('./input.txt', 'r') as f:
    d = f.read()
    d = d.strip().split('\n\n')
    d = [s.split('\n') for s in d]

e = 0

def g(s):
    u = 0
    for i in range(len(s) - 1):
        dif = 0
        for j in range(0, min(i + 1, len(s) - i - 1)):
            dif += sum([1 for k in range(len(s[0])) if s[i - j][k] != s[i + 1 + j][k]])
            if dif > 1:
                break
        if dif == 1:
            u += i + 1
    return u

for s in d:
    e += 100 * g(s)
    e += g(tuple(zip(*s)))

print(e)
