with open('./input.txt', 'r') as f:
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
m={}
for r in p:
    r=r.split(' -> ')
    m[r[0][1:]]=[r[0][0]=='%',r[1].split(', '),{}]
for k in m:
    for n in m[k][1]:
        if n in m and not m[n][0]:
            m[n][2][k]=0
def g(s,t,b):
    if not t in m:return
    if m[t][0] and not b:
        m[t][2]=not m[t][2]
        for n in m[t][1]:
            st.append((t,n,m[t][2]))
    elif not m[t][0]:
        m[t][2][s]=b
        for n in m[t][1]:
            st.append((t,n,not all(m[t][2].values())))
tl,th=0,0
for i in range(1000):
    tl+=1
    st=[("roadcaster",n,0) for n in m["roadcaster"][1]]
    while st:
        s,t,b=st.pop(0)
        if b:th+=1
        else:tl+=1
        g(s,t,b)
print(tl*th)
