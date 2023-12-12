import re
import itertools

with open('./input.txt', 'r') as f:
    d = f.readlines()
    d = [l.strip() for l in d]

total = 0

memo = {}

so = "#???#?????.?#?. 2,1,2,1"
def num_fits(s, n):
    if len(s) == 0 and len(n) != 0: return 0
    if len(n) == 0:
        for i in range(0, len(s)):
            if s[i].find('#') != -1: return 0
        return 1
    if len(s[0]) < n[0]:
        if s[0].find('#') != -1: res = 0
        else: res = num_fits(s[1:], n)
        memo[(".".join(s), ",".join(map(str, n)))] = res
        return res
    mem = memo.get((".".join(s), ",".join(map(str, n))))
    if mem is not None: return mem
    hashind = s[0].find('#')
    maxStart = len(s[0]) - n[0]
    if hashind != -1: maxStart = min(hashind, maxStart)
    subtotal = 0
    for i in range(0, maxStart + 1):
        if i + n[0] < len(s[0]) and s[0][i + n[0]] == '#': continue
        if i + n[0] + 1 >= len(s[0]):
            subtotal += num_fits(s[1:], n[1:])
        else:
            subtotal += num_fits([s[0][i + n[0] + 1:]] + s[1:], n[1:])
    if s[0].find('#') == -1:
        subtotal += num_fits(s[1:], n)
    memo[(".".join(s), ",".join(map(str, n)))] = subtotal
    return subtotal

count = 0
for r in d:
    [s, n] = r.split(' ')
    s = '?'.join([s] * 5)
    n = ','.join([n] * 5)
    s = s.replace('.', ' ').strip()
    s = re.split("\s+", s)
    n = list(map(int, n.split(',')))
    res = num_fits(s, n)
    total += res
    memo = {}
    count += 1

print(total)
