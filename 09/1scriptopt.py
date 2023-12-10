f = open('./input.txt', 'r')
d = f.readlines()

t = 0

def n(s):
    if len(s) == 0: return 0
    d = [x - s[i - 1] for i, x in enumerate(s) if i > 0]
    return s[-1] + n(d)

for l in d:
    l = [int(x) for x in l.split()]
    t += n(l)

print(t)
f.close()
