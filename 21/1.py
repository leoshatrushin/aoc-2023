with open('input.txt', 'r') as f:
    p=f.read().strip().split('\n')
    h,w=len(p),len(p[0])
from functools import cache, reduce
import operator
from itertools import product
import re
import heapq
import copy
def mv(i,j,d,n=1):
    if type(d)==str:
        if d.upper() in 'URDL': d = 'URDL'.index(d.upper())
        else: d = 'NEWS'.index(d.upper())
    return [(i-n,j),(i,j+n),(i+n,j),(i,j-n)][d]
v={}
for i, r in enumerate(p):
    for j, a in enumerate(r):
        if a=='S':v[0]={(i,j)}
def g(i,j,n):
    i,j=mv(i,j,d)
    if not 0<=i<h or not 0<=j<w:return
    if p[i][j]=='#':return
    if n+1 not in v: v[n+1]=set()
    v[n+1].add((i,j))
for n in range(64):
    for i,j in v[n]:
        for d in range(4):
            g(i,j,n)
print(len(v[64]))
