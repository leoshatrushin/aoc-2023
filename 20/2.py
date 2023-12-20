with open('./input.txt', 'r') as f:
    p=f.read().strip().split('\n')
    h,w=len(p),len(p[0])
from functools import cache, reduce
import operator
from itertools import product
import re
import heapq
import copy
import math
def mv(i,j,d,n=1):
    if type(d)==str:
        if d.upper() in 'URDL': d = 'URDL'.index(d.upper())
        else: d = 'NEWS'.index(d.upper())
    return [(i-n,j),(i,j+n),(i+n,j),(i,j-n)][d]
m={}
for r in p:
    r=r.split(' -> ')
    m[r[0][1:]]=[r[0][0]=='%',r[1].split(', ')]
m2={}
st=[("roadcaster",n) for n in m["roadcaster"][1]]
visited, rec_stack = set(), set()
def dfs2(k):
    if k in rec_stack:
        print(k)
        return True
    if k in visited:
        return False
    visited.add(k)
    rec_stack.add(k)
    for n in m[k][1]:
        if dfs2(n):
            return True
    rec_stack.remove(k)
    return False
print(any(dfs2(k) for k in m if k not in visited))
exit()
while st:
    s,t=st.pop()
    if t in m2:
        m2[t][1].append(s)
        if t in m:
            for n in m[t][1]:
                st.append((t,n))
    else:
        if t in m:
            m2[t]=[m[t][0],[s]]
            for n in m[t][1]:
                st.append((t,n))
        else:m2[t]=[True,[s]]
print("hi");exit()
m=m2
vis=set()
st=[]
def dfs(k):
    if k in vis:return
    vis.add(k)
    if k in m:
        for n in m[k][1]:
            dfs(n)
    st.append(k)
for k in m:
    dfs(k)
print(m)
sig={"roadcaster":[[0]]}
count=0
for k in st[1:]:
    if m[k][0]:state=0;statememo={0}
    else:state={n:0 for n in set(m[k][1])};statememo={"".join(map(str, state.values()))}
    sig[k]=[]
    cum=0
    while True:
        for i in range(math.lcm(*(len(sig[n]) for n in set(m[k][1])))):
            sig[k].append([])
            counts={n:0 for n in set(m[k][1])}
            for n in m[k][1]:
                p=sig[n][i%len(sig[n])][counts[n]]
                if k=="rx" and p==0:print(cum);exit()
                counts[n]+=1
                if m[k][0]:
                    if p==0:
                        state=0 if state else 1
                        sig[k][cum].append(1 if state else 0)
                    else:
                        sig[k][cum].append(-1)
                else:
                    if p!=-1:
                        state[n]=p
                        sig[k][cum].append(0 if all(v==1 for v in state.values()) else 1)
                    else:
                        sig[k][cum].append(-1)
            cum+=1
        if m[k][0]:
            if state in statememo:break
        else:
            if "".join(map(str, state.values())) in statememo:break
        if m[k][0]:statememo.add(state)
        else:statememo.add("".join(map(str, state.values())))
        print(statememo)
        count+=1
        if count==1:exit()
    print(sig)
