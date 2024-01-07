with open('input.txt', 'r') as f:
    p=f.read().strip().split('\n')
    h,w=len(p),len(p[0])
from functools import cache, reduce
import operator
from itertools import product
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
z=set(((0,1),(h-1,w-2)))
for i,r in enumerate(p):
    for j,c in enumerate(r):
        if p[i][j]=='#':continue
        if [0<=x<h and 0<=y<w and p[x][y]!='#' for x,y in [mv(i,j,d) for d in range(4)]].count(True)>=3:
            z.add((i,j))
l={}
for i,j in z:
    if (i,j) not in l:l[(i,j)]=[]
    for D in range(4):
        cont=0
        for _,_,_,d in l[(i,j)]:
            if D==d:cont=1
        if cont:continue
        v=set(((i,j),))
        x,y=mv(i,j,D)
        if not (0<=x<h and 0<=y<w and p[x][y]!='#'):continue
        u=0
        lastd=D
        while True:
            u+=1
            v.add((x,y))
            if (x,y) in z:
                l[(i,j)].append((u,x,y,D))
                if (x,y) not in l:l[(x,y)]=[]
                l[(x,y)].append((u,i,j,'2301'.index(str(lastd))));break
            stop=1
            for d in range(4):
                nx,ny=mv(x,y,d)
                if nx<0 or ny<0 or nx>=h or ny>=w:continue
                if p[nx][ny]=='#' or (nx,ny) in v:continue
                x,y=nx,ny
                stop=0
                lastd=d
                break
            if stop:break
v=set()
n=0
def g(i,j,t):
    global n
    if (i,j) in v: return
    v.add((i,j))
    if (i,j)==(h-1,w-2):
        if t>n:n=t
    else:
        for u,x,y,_ in l[i,j]:
            g(x,y,t+u)
    v.remove((i,j))
g(0,1,0)
print(n)
