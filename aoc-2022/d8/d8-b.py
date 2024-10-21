g = [l.strip() for l in open('data')]

t = []

y = 0
while y < len(g):
    x = 0
    while x < len(g[y]):
        ss = 1
        for d in ((-1,0),(0,1),(1,0),(0,-1)):
            xc = x + d[0]
            yc = y + d[1]
            s = 0
            while 0 <= xc and xc < len(g[y]) and 0 <= yc and yc < len(g):
                s += 1
                if g[yc][xc] >= g[y][x]:
                    break
                xc += d[0]
                yc += d[1]
            ss *= s
        t.append(ss)
        x += 1
    y += 1

print(max(t))
