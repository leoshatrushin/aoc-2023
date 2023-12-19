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
def i(k,c,v,o):
    o=copy.deepcopy(o)
    if c=='<':o[k][1]=min(o[k][1],v-1)
    if c=='>':o[k][0]=max(o[k][0],v+1)
    if o[k][0]>o[k][1]:return 0
    return o
def z(n,o):
    global t
    if n=='A':t+=reduce(operator.mul, (b-a+1 for a,b in o.values()), 1)
    elif n!='R':g(n,o)
def g(n,o):
    for r in m[n]:
        if ':' in r:
            r,n=r.split(':')
            k,c,v=r[0],r[1],int(r[2:])
            no=i(k,c,v,o)
            if no:z(n,no)
            o=i(k,'<' if c=='>' else '>',v+1 if c=='>' else v-1,o)
            if not o:break
        else:z(r,o)
t=0
m={}
for l in p[0].split():
    n,r=l.split('{')
    m[n]=r[:-1].split(',')
g('in',{a:[1,4000] for a in 'xmas'})
print(t)
