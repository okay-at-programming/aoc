path = open('data').read().strip()

sp = [(0,0),(0,0)]
i = 0
seen = set()
seen.add(sp[0])
for c in path:
    p = sp[i]
    if c == '^':
        p = p[0],p[1]+1
    elif c == '>':
        p = p[0] + 1,p[1]
    elif c == 'v':
        p = p[0],p[1]-1
    elif c == '<':
        p = p[0]-1,p[1]
    else:
        assert False

    seen.add(p)
    sp[i] = p
    i = (i+1)%2

print(len(seen))

