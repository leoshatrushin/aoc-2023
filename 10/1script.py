f = open('./input.txt', 'r')
d = f.readlines()

m = [];

Si = 0
Sj = 0

for i, l in enumerate(d):
    m.append([c for c in l.strip()])
    for j, t in enumerate(l):
        if t == 'S':
            Si = i
            Sj = j

li = 0
lj = 0
D = ""
if not m[max(Si - 1, 0)][Sj] in '.-JL': li = max(Si - 1, 0); lj = Sj; D = "D"
elif not m[min(Si + 1, len(m))][Sj] in '.-F7': li = min(Si + 1, len(m)); lj = Sj; D = "U"
elif not m[Si][max(Sj - 1, 0)] in '.|J7': li = Si; lj = max(Sj - 1, 0); D = "R"
else: li = Si; lj = min(Sj + 1, len(m[0])); D = "L"

t = 0
while True:
    t += 1
    tobreak = 0
    match (m[li][lj], D):
        case ("|", "D"): li -= 1
        case ("|", "U"): li += 1
        case ("-", "L"): lj += 1
        case ("-", "R"): lj -= 1
        case ("L", "U"): lj += 1; D = "L"
        case ("L", "R"): li -= 1; D = "D"
        case ("F", "D"): lj += 1; D = "L"
        case ("F", "R"): li += 1; D = "U"
        case ("J", "U"): lj -= 1; D = "R"
        case ("J", "L"): li -= 1; D = "D"
        case ("7", "D"): lj -= 1; D = "R"
        case ("7", "L"): li += 1; D = "U"
        case ("S", _) : break

print(int(t / 2))
f.close()
