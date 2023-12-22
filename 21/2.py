with open('input.txt', 'r') as f:
    p=f.read().strip().split('\n')
    h,w=len(p),len(p[0])
from functools import cache, reduce
from itertools import product
from collections import deque
import operator
import re
import heapq
import copy
def lo(t):
    for i, r in enumerate(p):
        for j, a in enumerate(r):
            if a==t:return i,j
def mv(i,j,d,n=1):
    if type(d)==str:
        if d.upper() in 'URDL': d = 'URDL'.index(d.upper())
        else: d = 'NEWS'.index(d.upper())
    return [(i-n,j),(i,j+n),(i+n,j),(i,j-n)][d]
nl=[(i,j) for i,j in product(*map(range,(h,w))) if p[i][j]!='#']
el=[(0,j)for j in range(w)]+[(h-1,j)for j in range(w)]+[(i,0)for i in range(1,h-1)]+[(i,w-1)for i in range(1,h-1)]
m={}
for i,r in enumerate(p):
    j=0
    for g in r.split('(#+)'):
        for a in g:
            if a=="#":m[i,j]={e:float('inf') for e in el}
        if g[0]=="#":j+=len(g);continue
