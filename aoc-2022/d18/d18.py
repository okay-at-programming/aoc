
ps = set()
for l in open('data'):
    p = tuple(int(x) for x in l.strip().split(','))
    ps.add(p)

t = 0
for x,y,z in ps:
    for dx,dy,dz in ((1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)):
        np = x+dx,y+dy,z+dz
        if np not in ps:
            t += 1
print(t)
