g = [l.strip() for l in open('data')]

t = set()

for d in ((-1,0),(0,1),(1,0),(0,-1)):

    y = 0
    while y < len(g):
        x = 0
        while x < len(g[y]):
            xc = x + d[0]
            yc = y + d[1]
            v = True
            while 0 <= xc and xc < len(g[y]) and 0 <= yc and yc < len(g):
                if g[yc][xc] >= g[y][x]:
                    v = False
                xc += d[0]
                yc += d[1]
            if v:
                t.add((x,y))
            x += 1
        y += 1

print(len(t))
