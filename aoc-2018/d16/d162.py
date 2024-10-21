
def get(line):
    s = line.index('[') + 1
    e = line.index(']')
    return [int(x) for x in line[s:e].split(', ')]

def comp(i, a, b, c, reg):
    r = [x for x in reg]
    if i == 0:
        r[c] = r[a] + r[b]
    elif i == 1:
        r[c] = r[a] + b
    elif i == 2:
        r[c] = r[a] * r[b]
    elif i == 3:
        r[c] = r[a] * b
    elif i == 4:
        r[c] = r[a] & r[b]
    elif i == 5:
        r[c] = r[a] & b
    elif i == 6:
        r[c] = r[a] | r[b]
    elif i == 7:
        r[c] = r[a] | b
    elif i == 8:
        r[c] = r[a]
    elif i == 9:
        r[c] = a
    elif i == 10:
        r[c] = 1 if a > r[b] else 0
    elif i == 11:
        r[c] = 1 if r[a] > b else 0
    elif i == 12:
        r[c] = 1 if r[a] > r[b] else 0
    elif i == 13:
        r[c] = 1 if r[a] == r[b] else 0
    elif i == 14:
        r[c] = 1 if r[a] == b else 0
    elif i == 15:
        r[c] = 1 if a == r[b] else 0
    else:
        print('error')
    return r

m = {i:[j for j in range(16)] for i in range(16)}
t = 0
start = None
expected = None
data = None
cont = True
prog = []
savprog = False
for line in open('data.txt'):
    if line.strip():
        cont = True
    elif not cont:
        savprog = True
    else:
        cont = False

    if savprog:
        if not line.strip():
            continue
        prog.append([int(x) for x in line.split(' ')])
        continue
    if line.startswith('Before'):
        start = get(line)
    elif line.startswith('After'):
        expected = get(line)
        x = data[0]
        n = []
        for i in m[x]:
            o = comp(i, data[1], data[2], data[3], start)
            if o == expected:
                n.append(i)
        m[x] = n
    elif line[0].isdigit():
        data = [int(x) for x in line.split(' ')]

proceed = True
while proceed:

    proceed = False
    torem = []

    for k,v in m.items():
        if len(v) > 1:
            proceed = True

        if len(v) == 1:
            torem.append(v[0])

    for j in torem:
        for v in m.values():
            if len(v) > 1 and j in v:
                v.remove(j)

mem = [0 for _ in range(4)]
for p in prog:
    mem = comp(m[p[0]][0], p[1], p[2], p[3], mem)

print(' '.join([str(x) for x in mem]))
