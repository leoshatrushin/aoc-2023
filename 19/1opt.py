with open('./input.txt', 'r') as f:
    p=f.read().strip().split('\n\n')
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
t=0
m={}
def z(n,o):
    global t
    if n=='A':t+=sum(o.values())
    elif n!='R':g(n,o)
def g(n,o):
    for r in m[n]:
        if ':' in r:
            r,n=r.split(':')
            if eval("o[r[0]]"+r[1:]):z(n,o);break
        else:z(r,o)
for l in p[0].split():
    n,r=l.split('{')
    m[n]=r[:-1].split(',')
for o in p[1].split():
    o={k:int(v) for k,v in [a.split('=') for a in o[1:-1].split(',')]}
    g('in',o)
print(t)
