import re
import itertools

with open('./input.txt', 'r') as f:
    d = f.readlines()
    d = [l.strip() for l in d]

total = 0

m = []

def fits(s, n):
    s = s.replace('.', ' ').strip()
    s = re.split("\s+", s)
    s = [len(x) for x in s]
    return s == n

count = 0
for r in d:
    [s, n] = r.split(' ')
    n = list(map(int, n.split(',')))
    ntot = sum(n)
    qind = [i for i, x in enumerate(s) if x == '?']
    nq = len(qind)
    nhash = len([t for t in s if t == '#'])
    subtotal = 0
    for locs in itertools.combinations(range(nq), ntot - nhash):
        sp = list(s)
        bin_list = ['#' if i in locs else '.' for i in range(nq)]
        for qi, bin in zip(qind, bin_list):
            sp[qi] = bin
        if fits(''.join(sp), n):
            subtotal += 1
    if (count == 20): break
    print(subtotal)
    count += 1
    total += subtotal

print(total)
