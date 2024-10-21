from collections import deque

fd = {}
f = 1
md = {}
gd = {}

for l in open('test'):
    l = l.strip().split()
    i = 0
    mcs = []
    gs = []
    while i < len(l):
        if l[i].startswith('microchip'):
            m = l[i-1].split('-')[0]
            mcs.append(m)
            md[m] = f
        if l[i].startswith('generator'):
            g = l[i-1]
            gs.append(g)
            gd[g] = f
        i += 1
    fd[f] = (mcs,gs)
    f += 1

def complete(md,gd):
    return all(x == 4 for x in md) and all(x == 4 for x in gd)

def valid(md, gd):
    for m in md:
        if md[m] == gd[m]:
            continue

        for o in md:
            if o == m:
                continue
            if md[o] == md[m]:
                return False
    return True

def on(f,md,gd):
    pass


q = deque()
q.append((1,md,gd,0))

while q:
    f,md,gd,s = q.popleft()

    if complete(md,gd):
        print(s)
        break

    if not valid(md,gd):
        continue






