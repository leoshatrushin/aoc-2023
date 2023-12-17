with open('./input.txt', 'r') as f:
    m=f.read().strip().split('\n')
    h,w=len(m),len(m[0])
from functools import cache
from itertools import product
import re
import heapq
m=[[int(a) for a in r] for r in m]
s=set()
q=[(-m[0][0],0,-1,1,-1)]
while q:
    l,i,j,d,n=heapq.heappop(q)
    i,j=[(i-1,j),(i,j+1),(i+1,j),(i,j-1)][d]
    if not 0<=i<h or not 0<=j<w:continue
    l+=m[i][j]
    n+=1
    if i==h-1 and j==w-1:print(l);break
    if (i,j,d,n) in s:continue
    s.add((i,j,d,n))
    for nd in range(4):
        if nd%2==d%2:continue
        heapq.heappush(q,(l,i,j,nd,0))
    if n<3:heapq.heappush(q,(l,i,j,d,n))
