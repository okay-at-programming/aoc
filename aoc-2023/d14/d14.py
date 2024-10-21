
g = [l.strip() for l in open('data')]
t=0
for x in range(len(g[0])):
    b = 0
    s = 0
    rc = 0
    for y in range(len(g)):
        if g[y][x] == 'O':
            rc += 1
        elif g[y][x] == '#':
            for i in range(rc):
                s += len(g) - (b + i)
            rc = 0
            b = y+1

    for i in range(rc):
        s += len(g) - (b + i)
    t += s

print(t)

