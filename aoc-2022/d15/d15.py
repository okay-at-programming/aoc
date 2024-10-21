
ri = 2000000
r = set()
sub = set()

for l in open('data'):
    s,b = l.split(':')
    sx = int(s.split('=')[1].split(',')[0])
    sy = int(s.split('=')[2])
    bx = int(b.split('=')[1].split(',')[0])
    by = int(b.split('=')[2])
    if by == ri:
        sub.add(bx)
    if sy == ri:
        sub.add(sx)

    md = abs(bx-sx) + abs(by-sy)

    d = abs(sy - ri)

    if md < d:
        continue

    l = md - d

    print(sx,sy, bx,by, sx-l, sx+l)

    for i in range(sx-l, sx + l + 1):
        r.add(i)

print(len(r-sub))
