with open('./input.txt', 'r') as f:
    d=f.read().strip().split('\n')
from functools import cache
from itertools import product
import re
import heapq
t=0
d=[list(map(int,list(r))) for r in d]
n={(i, j, U, R, D, L): float('inf') for i, j, U, R, D, L in product(*map(range, (len(d), len(d[0]), 4, 4, 4, 4)))}
s=(0,0,3,3,3,3)
n[s]=0
h=[(0, *s)]
def g(t):
    l,i,j,*_=t
    if i<0 or j<0 or i>=len(d) or j>=len(d[0]): return
    lp=l+d[i][j]
    if lp>=n[t[1:]]: return
    n[t[1:]]=lp
    heapq.heappush(h, (lp, *t[1:]))
while h:
    l,i,j,U,R,D,L=heapq.heappop(h)
    if l>n[i, j, U, R, D, L]: continue
    if U > 0 and D==3: g((l, i-1, j, U-1, 3, 3, 3))
    if R > 0 and L==3: g((l, i, j+1, 3, R-1, 3, 3))
    if D > 0 and U==3: g((l, i+1, j, 3, 3, D-1, 3))
    if L > 0 and R==3: g((l, i, j-1, 3, 3, 3, L-1))
print(min(n[len(d)-1, len(d[0])-1, U, R, D, L] for U,R,D,L in product(*map(range, (4, 4, 4, 4)))))
