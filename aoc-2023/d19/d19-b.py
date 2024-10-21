from collections import deque

wfs,prts = open('data').read().split('\n\n')
flows = {}

for l in wfs.split('\n'):
    n = l.split('{')[0]
    l = l.split('{')[1].split('}')[0]
    rs = []
    for r in l.split(','):
        if ':' in r:
            cmp = r.split(':')[0]
            dest = r.split(':')[1]
            if '<' in cmp:
                k,v = cmp.split('<')
                t = k,'<',int(v)
            elif '>' in cmp:
                k,v = cmp.split('>')
                t = k,'>',int(v)
            else:
                assert False
            rs.append((t,dest))
        else:
            rs.append((r,))
    flows[n] = rs


def ols(r,t,c):
    if r[0]<t<r[1]:
        if c == '<':
            return ((r[0],t),(t,r[1]))
        else:
            return ((t+1,r[1]),(r[0],t+1))
    elif r[0] < t:
        if c == '<':
            return (r,None)
        return (None,r)
    else:
        if c == '<':
            return (None,r)
        return (r,None)

q = deque()
m = {c:(1,4001) for c in 'xmas'}
m['k'] = 'in'
q.append(m)
t = 0
while q:
    m = q.popleft()

    k = m['k']

    while True:
        if k in 'AR':
            break
        fl = flows[k]
        for rl in fl:
            if len(rl) == 2:
                cmp,dest = rl
                i,o = ols(m[cmp[0]],cmp[2],cmp[1])
                im = {k:v for k,v in m.items()}
                if i:
                    im[cmp[0]] = i
                    im['k'] = dest
                    q.append(im)
                if o:
                    m[cmp[0]] = o
            elif len(rl) == 1:
                m['k'] = rl[0]
                k = rl[0]
            else:
                assert False, rl

    if k == 'A':
        r = 1
        for k,v in m.items():
            if k in 'xmas':
                r *= (v[1]-v[0])
        t += r

print(t)
