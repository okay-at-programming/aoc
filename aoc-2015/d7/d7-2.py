rules = [l.strip() for l in open('data2')]

wires = {}
seen = set()
t = 0
lt = -1

def get(a):
    if a.isnumeric():
        return int(a)
    return wires[a]

def getable(a):
    return a.isnumeric() or a in wires

while True:
    for index,rule in enumerate(rules):
        if index in seen:
            continue
        i,o = [x.strip() for x in rule.split('->')]

        if getable(i):
            wires[o] = get(i)
            seen.add(index)
        elif 'AND' in i:
            a,_,b = i.split()
            if getable(a) and getable(b):
                wires[o] = get(a) & get(b)
                seen.add(index)
        elif 'OR' in i:
            a,_,b = i.split()
            if getable(a) and getable(b):
                wires[o] = get(a) | get(b)
                seen.add(index)
        elif 'LSHIFT' in i:
            a,_,b = i.split()
            if getable(a):
                wires[o] = get(a) << int(b)
                seen.add(index)
        elif 'RSHIFT' in i:
            a,_,b = i.split()
            if getable(a):
                wires[o] = get(a) >> int(b)
                seen.add(index)
        elif 'NOT' in i:
            _,a = i.split()
            if getable(a):
                wires[o] = (1 << 16) - 1 - get(a)
                seen.add(index)

    print(t, len(seen), len(rules))
    t += 1
    if lt == len(seen):
        print('error')
        break
    lt = len(seen)

    if len(rules) == len(seen):
        break



print(wires)
