with open('./input.txt', 'r') as f:
    p=f.read().strip().split('\n\n')
    h,w=len(p),len(p[0])
from functools import cache
from itertools import product
import re
import heapq
def mv(i,j,d,n=1):
    if type(d)==str:
        if d.upper() in 'URDL': d = 'URDL'.index(d.upper())
        else: d = 'NEWS'.index(d.upper())
    return [(i-n,j),(i,j+n),(i+n,j),(i,j-n)][d]
t=0
m={}
for l in p[0].split():
    n,r=l.split('{')
    m[n]=r[:-1].split(',')
l=[]
for o in p[1].split():
    o={k:int(v) for k,v in [a.split('=') for a in o[1:-1].split(',')]}
    l+=[o]
def go(n,o):
    global t
    if n=='R':return
    if n=='A':t+=sum(o.values());return
    do(n,o)
def do(n,o):
    for r in m[n]:
        if '>' in r or '<' in r:
            r,n=r.split(':')
            if '<' in r:p,c,v=re.split('(<)', r)
            else:p,c,v=re.split('(>)', r)
            if c=='<' and o[p]<int(v):go(n,o);break
            if c=='>' and o[p]>int(v):go(n,o);break
        else:go(r,o);break
for o in l:
    do('in',o)
print(t)
