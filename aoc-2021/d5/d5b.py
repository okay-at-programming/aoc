ps = {}

for l in open('data'):
    p1,p2 = l.strip().split(' -> ')
    x1,y1 = [int(x) for x in p1.split(',')]
    x2,y2 = [int(x) for x in p2.split(',')]

    if x1 == x2 and y1 != y2:
        if y1 > y2:
            y1,y2 = y2,y1
        for y in range(y1,y2+1):
            ps[(x1,y)] = ps.get((x1,y),0) + 1
    elif y1 == y2 and x1 != x2:
        if x1 > x2:
            x1,x2 = x2,x1
        for x in range(x1,x2+1):
            ps[(x,y1)] = ps.get((x,y1),0) + 1
    else:
        if x1 > x2:
            x1,x2 = x2,x1
            y1,y2 = y2,y1
        d = 1 if y1 < y2 else -1
        for i in range(0,x2-x1+1):
            x = x1+i
            y = y1 + (d*i)
            ps[(x,y)] = ps.get((x,y),0) + 1

s = 0
for p in ps.values():
    if p > 1:
        s +=1

print(s)

