m,pas = open('data').read().split('\n\n')


g = {}
y = 1
for l in m.split('\n'):
    x = 1
    for c in l:
        if c in ('#','.'):
            g[(x,y)] = c
        x += 1
    y += 1

p = min(x for x,y in g.keys() if y == 1),1
d = 0

dirs = ((1,0),(0,1),(-1,0),(0,-1))
off = (lambda i,j: (min(x for x,y in g.keys() if y == j),j),
       lambda i,j: (i,min(y for x,y in g.keys() if x == i)),
       lambda i,j: (max(x for x,y in g.keys() if y == j),j),
       lambda i,j: (i,max(y for x,y in g.keys() if x == i)))


i = 0
while i < len(pas):
    j = i
    while pas[j].isnumeric():
        j += 1
    steps = int(pas[i:j])
    i = j

    for _ in range(steps):
        np = p[0]+dirs[d][0],p[1]+dirs[d][1]

        if np not in g:
            np = off[d](np[0],np[1])

        if g[np] == '#':
            np = p
        else:
            p = np

    if pas[i] == 'R':
        d = (d+1)%4
    elif pas[i] == 'L':
        d = (d-1)%4
    i += 1

print(1000*p[1]+4*p[0]+d)

