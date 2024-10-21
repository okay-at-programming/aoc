
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

print(flows)
t = 0

for l in prts.strip().split('\n'):
    l = l[1:-1]
    m = {p.split('=')[0]:int(p.split('=')[1])for p in l.split(',')}
    k = 'in'
    o = ''
    print(m)

    while not o:
        if k in 'AR':
            o = k
            continue
        fl = flows[k]
        for rl in fl:
            if len(rl) == 2:
                cmp,dest = rl
                if cmp[1] == '<':
                    if m[cmp[0]] < cmp[2]:
                        k = dest
                        break
                elif cmp[1] == '>':
                    if m[cmp[0]] > cmp[2]:
                        k = dest
                        break
                else:
                    assert False
            elif len(rl) == 1:
                k = rl[0]
            else:
                assert False, rl

    if o == 'A':
        t += sum(m.values())

print(t)
