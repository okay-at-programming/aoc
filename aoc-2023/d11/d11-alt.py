from collections import deque

gs = set()

data = [l.strip() for l in open('data')]
mult1 = 1
mult2 = 1000000-1

brws = set()
bcs = set()

for y,l in enumerate(data):
    for x,c in enumerate(l):
        if c == '#':
            brws.add(y)
            bcs.add(x)
            gs.add((x,y))


maxx = max(x for x,_ in gs)
maxy = max(y for _,y in gs)

ld = list(gs)

total1 = 0
total2 = 0
for i,p in enumerate(ld):
    for op in ld[i+1:]:
        d = abs(p[0]-op[0]) + abs(p[1]-op[1])
        ex1 = sum([mult1 for v in range(min(p[0],op[0]),max(p[0],op[0])) if v not in bcs])
        ex2 = sum([mult2 for v in range(min(p[0],op[0]),max(p[0],op[0])) if v not in bcs])
        ey1 = sum([mult1 for v in range(min(p[1],op[1]),max(p[1],op[1])) if v not in brws])
        ey2 = sum([mult2 for v in range(min(p[1],op[1]),max(p[1],op[1])) if v not in brws])
        total1 += d + ex1 + ey1
        total2 += d + ex2 + ey2

print(total1)
print(total2)
