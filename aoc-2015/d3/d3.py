path = open('data').read().strip()

p = 0,0
seen = set()
twice = set()
seen.add(p)
for c in path:
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

    if p in seen:
        twice.add(p)
    seen.add(p)

print(len(seen))
print(len(twice))

