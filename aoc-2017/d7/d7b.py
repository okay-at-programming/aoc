prog = {}

for line in open('data'):
    pn = line.split()[0].strip()
    w = int(line.split()[1][1:-1])
    if '>' in line:
        deps = [x.strip() for x in line.split('>')[1].strip().split(',')]
        prog[pn] = w,deps
    else:
        prog[pn] = w,[]

for key in prog.keys():
    found = True
    for c,l in prog.values():
        if key in l:
            found = False
            break
    if found:
        base = key

weights = {}

def getweight(key):
    w = prog[key][0]
    for subkey in prog[key][1]:
        w += getweight(subkey)
    weights[key] = w
    return w

getweight(base)

def isbalanced(key):
    ws = {}
    for subkey in prog[key][1]:
        w = weights[subkey]
        l = ws.get(w,[])
        l.append(subkey)
        ws[w] = l
    if len(ws) == 2:
        for k in ws.values():
            if len(k) == 1:
                return k[0]
    return None

key = base
last = None
while True:
    c = isbalanced(key)
    if not c:
        break
    last = key
    key = c

for sub in prog[last][1]:
    print(sub, prog[sub][0], weights[sub])

