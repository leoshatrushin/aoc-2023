f = open('./input.txt', 'r')
d = f.readlines()
map(lambda x: x.strip(), d)
t = 0

emptycols = []
emptyrows = []
for i, l in enumerate(d):
    if all([c == '.' for c in l.strip()]):
        emptyrows.append(i)

for j in range(len(d[0])):
    if all([d[i][j] == '.' for i in range(len(d))]):
        emptycols.append(j)

galaxies = []
for i, l in enumerate(d):
    for j, c in enumerate(l):
        if c == '#':
            galaxies.append((i, j))

EMPTY_MOD = 1000000
for i, g in enumerate(galaxies):
    for h in galaxies[i+1:]:
        mini = min(g[0], h[0])
        maxi = max(g[0], h[0])
        minj = min(g[1], h[1])
        maxj = max(g[1], h[1])
        emptyrowmod = 0
        emptycolmod = 0
        for r in emptyrows:
            if mini < r < maxi:
                emptyrowmod += EMPTY_MOD - 1
        for c in emptycols:
            if minj < c < maxj:
                emptycolmod += EMPTY_MOD - 1
        t += abs(g[0] - h[0]) + abs(g[1] - h[1]) + emptyrowmod + emptycolmod

print(t)
f.close()
