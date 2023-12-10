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

if (left and (up or down)) or (right and (up or down)):
    m[Si][Sj] = "B"
if down: lastverticalTurn = "D"
elif up: lastverticalTurn = "U"
else:
    mj = Sj + 1
    while m[li][mj] == "-":
        mj += 1
    if m[li][mj] == "J":
        lastverticalTurn = "U"
    else:
        lastverticalTurn = "D"
while True:
    tobreak = 0
    match (m[li][lj], D):
        case ("|", "D"): m[li][lj] = "B"; li -= 1
        case ("|", "U"): m[li][lj] = "B"; li += 1
        case ("-", "L"): m[li][lj] = "H"; lj += 1
        case ("-", "R"): m[li][lj] = "H"; lj -= 1
        case ("L", "U"): m[li][lj] = "B"; lj += 1; D = "L"; lastverticalTurn = "U"
        case ("L", "R"):
            if lastverticalTurn == "U":
                m[li][lj] = "B"
            else:
                m[li][lj] = "H"
            li -= 1; D = "D"
        case ("F", "D"): m[li][lj] = "B"; lj += 1; D = "L"; lastverticalTurn = "D"
        case ("F", "R"):
            if lastverticalTurn == "D":
                m[li][lj] = "B"
            else:
                m[li][lj] = "H"
            li += 1; D = "U"
        case ("J", "U"): m[li][lj] = "B"; lj -= 1; D = "R"; lastverticalTurn = "U"
        case ("J", "L"):
            if lastverticalTurn == "U":
                m[li][lj] = "B"
            else:
                m[li][lj] = "H"
            li -= 1; D = "D"
        case ("7", "D"): m[li][lj] = "B"; lj -= 1; D = "R"; lastverticalTurn = "D"
        case ("7", "L"):
            if lastverticalTurn == "D":
                m[li][lj] = "B"
            else:
                m[li][lj] = "H"
            li += 1; D = "U"
        case ("B", _) : break

# for l in m:
#     print("".join(l))

t = 0
inloop = False
for l in m:
    for c in l:
        if c == "B":
            inloop = not inloop
            continue
        if c != "H" and inloop:
            t += 1

print(t)
f.close()
