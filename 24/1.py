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
t=0
l=[]
for i,r in enumerate(p):
    r=r.replace(' @',',')
    l.append([int(x) for x in r.split(', ')])
for i,a in enumerate(l):
    for b in l[i+1:]:
        u=np.array([[a[3],-b[3]],[a[4],-b[4]]])
        v=np.array([b[0]-a[0],b[1]-a[1]])
        x,*_=np.linalg.lstsq(u,v,rcond=None)
        if x[0]>=0 and x[1]>=0 and np.allclose(u@x,v):
            x,y=a[0]+a[3]*x[0],a[1]+a[4]*x[0]
            if 200000000000000<=x<=400000000000000 and 200000000000000<=y<=400000000000000:
                t+=1
print(t)
