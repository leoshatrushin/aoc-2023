with open('./input.txt', 'r') as f:
    d=f.read().strip().split('\n')
from functools import cache
from itertools import product
import re
import heapq
t=0
d=[list(map(int,list(r))) for r in d]
n={(i, j, c, D): float('inf') for i, j, c, D in product(*map(range, (len(d), len(d[0]), 11, 4)))}
s=(0,0,0,0)
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
    l,i,j,c,D=heapq.heappop(h)
    if l>n[i,j,c,D]: continue
    if (c == 0 or (c < 10 and D==0) or (c > 3 and D in [1,3]) and i > 3): g((l, i-1, j, c+1 if D == 0 else 1, 0))
    if (c == 0 or (c < 10 and D==1) or (c > 3 and D in [0,2]) and j < len(d[0]) - 4): g((l, i, j+1, c+1 if D == 1 else 1, 1))
    if (c == 0 or (c < 10 and D==2) or (c > 3 and D in [1,3]) and i < len(d) - 4): g((l, i+1, j, c+1 if D == 2 else 1, 2))
    if (c == 0 or (c < 10 and D==3) or (c > 3 and D in [0,2]) and j > 3): g((l, i, j-1, c+1 if D == 3 else 1, 3))
print(min(n[len(d)-1,len(d[0])-1,c,D] for c,D in product(*map(range, (11, 4))))) 
