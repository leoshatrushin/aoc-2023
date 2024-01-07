with open('input.txt', 'r') as f:
    p=f.read().strip().split('\n')
    h,w=len(p),len(p[0])
from functools import cache, reduce
from itertools import product
import numpy as np
import operator
import re
import heapq
import copy
import sys
sys.setrecursionlimit(10000)
def mv(i,j,d,n=1):
    if type(d)==str:
        if d.upper() in 'URDL': d = 'URDL'.index(d.upper())
        elif d.upper() in 'NEWS': d = 'NEWS'.index(d.upper())
        else: d = '^>v<'.index(d)
    return [(i-n,j),(i,j+n),(i+n,j),(i,j-n)][d]
l={}
n,m=set(),set()
for i,r in enumerate(p):
    k,v=r.split(': ')
    l[k]=v.split()
t=0
c=0
d=set()
f={}
def dfs(l):
    for u in l:
        if not u in d:
            dfsv(l,u)
def dfsv(l,u):
    global t,c
    t+=1
    c+=1
    d.add(u)
    for v in l[u]:
        if not v in d:
            dfsv(l,v)
    t+=1
    f[u]=t
for u in l:
    for v in l[u]:
        o=copy.deepcopy(l)
        o[u].remove(v)
        dfs(o)
        if c<len(l):
            print(c*(len(l)-c));exit()

