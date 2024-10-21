ps = {}

for l in open('data'):
    p1,p2 = l.strip().split(' -> ')
    x1,y1 = [int(x) for x in p1.split(',')]
    x2,y2 = [int(x) for x in p2.split(',')]

    if x1 == x2:
        if y1 > y2:
            y1,y2 = y2,y1
        for y in range(y1,y2+1):
            ps[(x1,y)] = ps.get((x1,y),0) + 1
    if y1 == y2:
        if x1 > x2:
            x1,x2 = x2,x1
        for x in range(x1,x2+1):
            ps[(x,y1)] = ps.get((x,y1),0) + 1

s = 0
for p in ps.values():
    if p > 1:
        s +=1

print(s)

