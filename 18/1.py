with open('./tinput.txt', 'r') as f:
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
    d,n,_=r.split()
    n=int(n)
    if d=='U':a+=j*n
    if d=='D':a-=j*n
    b+=n
    i,j=mv(i,j,d,n)
print(abs(a)+b//2+1)
