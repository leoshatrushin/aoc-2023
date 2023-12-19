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
def i(dom,p,c,v):
    dom=copy.deepcopy(dom)
    if c=='<':dom[p][1]=min(dom[p][1],v-1)
    if c=='>':dom[p][0]=max(dom[p][0],v+1)
    if dom[p][0]>dom[p][1]:return 0
    return dom
def go(dom,n):
    global t
    if n=='R' or not dom:return
    if n=='A':t+=reduce(operator.mul, (b-a+1 for a,b in dom.values()), 1);return
    do(dom,n)
def do(dom,n):
    for r in m[n]:
        if '>' in r or '<' in r:
            r,n=r.split(':')
            p,c,v=r[0],r[1],int(r[2:])
            ndom=i(dom,p,c,v)
            go(ndom,n)
            dom=i(dom,p,'<' if c=='>' else '>',v+1 if c=='>' else v-1)
            if not dom:break
        else:go(dom,r)
t=0
m={}
for l in p[0].split():
    n,r=l.split('{')
    m[n]=r[:-1].split(',')
do({a:[1,4000] for a in 'xmas'},'in')
print(t)
