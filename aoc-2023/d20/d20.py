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


lc = 0
hc = 0
for _ in range(1000):
    q = deque([('broadcaster',0,0)])
    while q:
        t,f,s = q.popleft()

        if f == 0:
            lc += 1
        else:
            hc += 1

        if t not in m:
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

print(lc,hc,lc*hc)
