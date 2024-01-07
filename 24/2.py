with open('input.txt', 'r') as F:
    p=F.read().strip().split('\n')
    h,w=len(p),len(p[0])

from functools import cache, reduce
from itertools import product
import numpy as np
import operator
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

t=0
l=[]

for i,r in enumerate(p):
    r=r.replace(' @',',')
    l.append([int(x) for x in r.split(', ')])

from z3 import *
def f(s):
  return Real(s)
x,y,z,vx,vy,vz = f('x'),f('y'),f('z'),f('vx'),f('vy'),f('vz')
T = [f(f'T{i}') for i in range(len(l))]
SOLVE = Solver()
for i,a in enumerate(l):
  SOLVE.add(x + T[i]*vx - l[0] - T[i]*l[3] == 0)
  SOLVE.add(y + T[i]*vy - l[1] - T[i]*l[4] == 0)
  SOLVE.add(z + T[i]*vz - l[2] - T[i]*l[5] == 0)
res = SOLVE.check()
M = SOLVE.model()
print(M.eval(x))
print(M.eval(y))
print(M.eval(z))
print(M.eval(x+y+z))
