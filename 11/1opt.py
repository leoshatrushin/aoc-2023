with open('./input.txt', 'r') as f:
    d = f.readlines()
    d = [l.strip() for l in d]

t = 0

emptyrows = [i for i, r in enumerate(d) if all([t == '.' for t in r])]
emptycols = [j for j, c in enumerate(zip(*d)) if all([t == '.' for t in c])]
galaxies = [(i, j) for i, r in enumerate(d) for j, t in enumerate(r) if t == '#']

for i, g in enumerate(galaxies):
    for h in galaxies[i+1:]:
        t += abs(g[0] - h[0]) + abs(g[1] - h[1])
        for r in emptyrows:
            if min(g[0], h[0]) < r < max(g[0], h[0]):
                t += 1
        for c in emptycols:
            if min(g[1], h[1]) < c < max(g[1], h[1]):
                t += 1

print(t)
