with open('input.txt', 'r') as f:
    p=f.read().strip().split('\n')
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
t=0
m=[]
x=[[0,0],[0,0],[0,0]]
y={}
for r in p:
    [s,e]=[list(map(int,a.split(','))) for a in r.split('~')]
    for i in range(3):
        x[i][0]=min(x[i][0],s[i],e[i])
        x[i][1]=max(x[i][1],s[i],e[i])
m=[[[0]*(x[1][1]+1-x[1][0]) for _ in range(x[0][0], x[0][1]+1)] for _ in range(x[2][1]+1)]
z={}
for b,r in enumerate(p):
    [s,e]=[list(map(int,a.split(','))) for a in r.split('~')]
    y[b+1]=[[min(s[0],e[0]),max(s[0],e[0])],[min(s[1],e[1]),max(s[1],e[1])],[min(s[2],e[2]),max(s[2],e[2])]]
    for i in range(y[b+1][0][0],y[b+1][0][1]+1):
        for j in range(y[b+1][1][0],y[b+1][1][1]+1):
            for k in range(y[b+1][2][0],y[b+1][2][1]+1):
                m[k][i][j]=b+1
    cz=min(s[2],e[2])
    if not cz in z: z[cz]=[b+1]
    else: z[cz].append(b+1)
def printm():
    for i in range(x[2][1]+1):
        print('z=',i)
        for j in range(x[0][1]+1):
            print(''.join(map(str,m[i][j])))
for cz in range(1,x[2][1]+1):
    if not cz in z: continue
    for b in z[cz].copy():
        maxz=0
        for i in range(min(y[b][0]),max(y[b][0])+1):
            for j in range(min(y[b][1]),max(y[b][1])+1):
                for nz in range(cz-1,maxz,-1):
                    if m[nz][i][j]:maxz=nz;break
        for i in range(min(y[b][0]),max(y[b][0])+1):
            for j in range(min(y[b][1]),max(y[b][1])+1):
                for dz in range(0,max(y[b][2])+1-min(y[b][2])):
                    m[cz+dz][i][j]=0
                    m[maxz+1+dz][i][j]=b
        z[cz].remove(b)
        if not cz in z: del z[cz]
        if not maxz+1 in z: z[maxz+1]=[b]
        else: z[maxz+1].append(b)
n={}
for cz in range(x[2][1],0,-1):
    if not cz in z: continue
    for b in z[cz]:
        n[b]=[]
        for i in range(min(y[b][0]),max(y[b][0])+1):
            for j in range(min(y[b][1]),max(y[b][1])+1):
                if m[cz-1][i][j]:n[b].append(m[cz-1][i][j])
@cache
def o(cz,l):
    if not cz in z:
        if cz==x[2][1]:return len(l)
        else:return o(cz+1,l)
    l = list(l)
    for b in z[cz]:
        if all([b2 in l for b2 in n[b]]):
            l.append(b)
    l = tuple(l)
    if cz==x[2][1]:return len(l)
    return o(cz+1,l)
for cz in range(1,x[2][1]+1):
    if not cz in z: continue
    for b in z[cz]:
        u=o(cz+1,(b,))-1
        t+=u
print(t)
