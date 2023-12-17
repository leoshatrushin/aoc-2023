with open('./input.txt', 'r') as f:
    d=f.read().strip().split('\n')
from functools import cache
from itertools import product
import re
import heapq
d=[list(map(int,list(r))) for r in d]
s=(0,0,-1,1)
n={(i,j,c,D):float('inf') for i,j,c,D in product(*map(range,(len(d),len(d[0]),10,4)))}
n[s]=0
h=[(0,*s)]
def g(l,i,j,c,D,Dp):
    if Dp!=D:
        if c!=-1 and c<3:return
        if Dp==0 and i<4:return
        if Dp==1 and j>len(d[0])-5:return
        if Dp==2 and i>len(d)-5:return
        if Dp==3 and j<4:return
    c=c+1 if Dp==D else 0
    if c==10: return
    i,j=[(i-1,j),(i,j+1),(i+1,j),(i,j-1)][Dp]
    if not 0<=i<len(d) or not 0<=j<len(d[0]): return
    lp=l+d[i][j]
    if lp>=n[i,j,c,Dp]: return
    n[i,j,c,Dp]=lp
    heapq.heappush(h,(lp,i,j,c,Dp))
while h:
    l,i,j,c,D=heapq.heappop(h)
    if l>n[i,j,c,D]: continue
    for Dp in range(4):
        if Dp!=D and Dp%2==D%2: continue
        g(l,i,j,c,D,Dp)
print(min(n[len(d)-1,len(d[0])-1,c,D] for c,D in product(*map(range,(10,4)))))
