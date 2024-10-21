
mc = 4000000

points = set()
areas = []

for l in open('data'):
    s,b = l.split(':')
    sx = int(s.split('=')[1].split(',')[0])
    sy = int(s.split('=')[2])
    bx = int(b.split('=')[1].split(',')[0])
    by = int(b.split('=')[2])

    md = abs(bx-sx) + abs(by-sy)

    points.update([(sx+i,sy-md-1+i) for i in range(md+1)])
    points.update([(sx+md+1-i,sy+i) for i in range(md+1)])
    points.update([(sx-i,sy+md+1-i) for i in range(md+1)])
    points.update([(sx-md-1+i,sy+i) for i in range(md+1)])

    areas.append((sx,sy,md))

print(len(points),len(areas))

for x,y in points:
    if 0<=x<=mc and 0<=y<=mc:
        v = True
        for sx,sy,md in areas:
            if abs(sx-x) + abs(sy-y) <= md:
                v = False
                break
        if v:
            print(x,y, 4000000*x + y)
            break
