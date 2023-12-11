f = open('./input.txt', 'r')
d = f.readlines()
t = 0

m = []
for l in d:
    m.append(l.strip())
    if all([c == '.' for c in l.strip()]):
        m.append(l.strip())

m2 = ["" for _ in range(len(m))]
for j in range(len(m[0])):
    for i in range(len(m)):
        m2[i] += m[i][j]
    if all([m[i][j] == '.' for i in range(len(m))]):
        for i in range(len(m)):
            m2[i] += m[i][j]

galaxies = []
for i, l in enumerate(m2):
    for j, c in enumerate(l):
        if c == '#':
            galaxies.append((i, j))

for i, g in enumerate(galaxies):
    for h in galaxies[i+1:]:
        t += abs(g[0] - h[0]) + abs(g[1] - h[1])

print(t)
f.close()
