with open('./input.txt', 'r') as f:
    p=f.read().strip().split('\n')
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
i,j,a,b=0,0,0,0
for r in p:
    s=r.split()[2]
    n=int(s[2:-2], 16)
    d=int(s[-2])
    if d==0:a-=j*n
    if d==2:a+=j*n
    b+=n
    i,j=mv(i,j,d,n)
print(abs(a)+b//2+1)
