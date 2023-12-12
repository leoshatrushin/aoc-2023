import re
import itertools
from functools import cache

with open('./input.txt', 'r') as F:
    d = F.readlines()
    d = [r.strip() for r in d]

e = 0

@cache
def f(s, n):
    if not n: return 0 if '#' in s else 1
    if len(s) < n[0]: return 0 
    if s[0] == '.': return f(s[1:], n)
    if s[0] == '#':
        if all(s[i] != '.' for i in range(n[0])) and \
            (len(s) == n[0] or s[n[0]] != '#'):
            return f(s[n[0] + 1:], n[1:])
        return 0
    return f(s[1:], n) + f('#' + s[1:], n)

for r in d:
    s,n=r.split()
    n=tuple(map(int, n.split(',')))
    e+=f(s, n)

print(e)
