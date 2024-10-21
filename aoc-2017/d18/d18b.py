from collections import deque

regs = ({'p':0,'snd':deque()},{'p':1,'snd':deque()})

def num(i):
    try:
        int(i)
    except ValueError:
        return False
    return True

def get(i,p):
    if num(i):
        return int(i)
    return regs[p].get(i, 0)

instructions = [l.strip() for l in open('data')]

def comp(p, l, c):
    if l < 0 or l >= len(instructions):
        return None
    ins = instructions[l]
    #print(p,l,ins)
    i = ins.split()[0]
    if i == 'snd':
        a = ins.split()[1]
        if p == 1:
            c += 1
        regs[(p+1)%2]['snd'].append(get(a,p))
    elif i == 'set':
        a = ins.split()[1]
        b = ins.split()[2]
        regs[p][a] = get(b,p)
    elif i == 'add':
        a = ins.split()[1]
        b = ins.split()[2]
        regs[p][a] = get(a,p) + get(b,p)
    elif i == 'mul':
        a = ins.split()[1]
        b = ins.split()[2]
        regs[p][a] = get(a,p) * get(b,p)
    elif i == 'mod':
        a = ins.split()[1]
        b = ins.split()[2]
        regs[p][a] = get(a,p) % get(b,p)
    elif i == 'rcv':
        a = ins.split()[1]
        r = regs[p]['snd']
        if len(r) == 0:
            return None
        regs[p][a] = r.pop()
    elif i == 'jgz':
        a = ins.split()[1]
        b = ins.split()[2]
        if get(a,p) > 0:
            l += (get(b,p) - 1)
    return l + 1, c

l = [0,0]
ap = 0
dl = [False, False]
dlc = 0
c = 0
cd = 0


while True:
    if dl[0] and dl[1]:
        dlc += 1
        if dlc > 10:
            break
    nl = comp(ap,l[ap],c)
    if nl == None:
        dl[ap] = True
        ap = (ap+1)%2
        continue
    dl[ap] = False
    dlc = 0
    l[ap],c = nl

    print(c)

print(c)


