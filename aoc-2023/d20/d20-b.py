from collections import deque

m = {}

for l in open('data'):
    l = l.strip().split()

    if l[0] == 'broadcaster':
        m[l[0]] = [l[0],[c.replace(',','') for c in l[2:]],'b']
    elif l[0].startswith('%'):
        n = l[0][1:]
        m[n] = [0,[c.replace(',','') for c in l[2:]],'%']
    elif l[0].startswith('&'):
        n = l[0][1:]
        m[n] = [{},[c.replace(',','') for c in l[2:]],'&']

for k,v in m.items():
    for o in v[1]:
        if o in m and m[o][2] == '&':
            m[o][0][k] = 0

sks = {k:0 for k in m['nr'][0].keys()}

lc = 0
r = 2
while True:
    q = deque([('broadcaster',0,0)])
    lc += 1
    while q:
        t,f,s = q.popleft()

        if t in sks:
            if f == 0 and sks[t] == 0:
                sks[t] = lc

        if t not in m:
            if t == 'rx' and f == 0:
                break
            continue
        elif t == 'broadcaster':
            for o in m[t][1]:
                q.append((o,f,t))
        elif m[t][2] == '%':
            if f == 0:
                ns = (m[t][0]+1)%2
                for o in m[t][1]:
                    q.append((o,ns,t))
                m[t][0] = ns
        elif m[t][2] == '&':
            m[t][0][s] = f
            if set(m[t][0].values()) == {1}:
                ns = 0
            else:
                ns = 1
            for o in m[t][1]:
                q.append((o,ns,t))
    br = True
    for k,v in sks.items():
        if v == 0:
            br = False

    if br:
        break

def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

def lcm(x,y):
    return (x*y)//gcd(x,y)

def lcml(l):
    x = 1
    for y in l:
        x = lcm(x,y)
    return x

print(lcml(list(sks.values())))
