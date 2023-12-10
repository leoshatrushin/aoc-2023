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
left = not m[Si][max(Sj - 1, 0)] in '.|J7'
right = not m[Si][min(Sj + 1, len(m[0]))] in '.|LF'
up = not m[max(Si - 1, 0)][Sj] in '.-JL'
down = not m[min(Si + 1, len(m))][Sj] in '.-F7'
if left: li = Si; lj = max(Sj - 1, 0); D = "R"
elif right: li = Si; lj = min(Sj + 1, len(m[0])); D = "L"
elif up: li = max(Si - 1, 0); lj = Sj; D = "D"
elif down: li = min(Si + 1, len(m)); lj = Sj; D = "U"

r = {
    "-": "1",
    "|": "2",
    "L": "3",
    "J": "4",
    "F": "5",
    "7": "6",
}

while True:
    oli = li
    olj = lj
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
    m[oli][olj] = r[m[oli][olj]]

if left and right: m[Si][Sj] = r["-"]
elif up and down: m[Si][Sj] = r["|"]
elif right and up: m[Si][Sj] = r["L"]
elif left and up: m[Si][Sj] = r["J"]
elif right and down: m[Si][Sj] = r["F"]
elif left and down: m[Si][Sj] = r["7"]

t = 0
inloop = False
lastvertical = ""
for l in m:
    for c in l:
        if c == r["-"]: continue
        if c in [r["|"], r["L"], r["F"]]:
            inloop = not inloop
            if c == r["L"]:
                lastvertical = "L"
            elif c == r["F"]:
                lastvertical = "F"
            continue
        if c == r["J"]:
            if lastvertical == "L": inloop = not inloop
            continue
        if c == r["7"]:
            if lastvertical == "F": inloop = not inloop
            continue
        if inloop: t += 1

print(t)
f.close()
