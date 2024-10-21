from collections import deque

ps = set()
for l in open('data'):
    p = tuple(int(x) for x in l.strip().split(','))
    ps.add(p)

minx = min(x for x,y,z in ps)
maxx = max(x for x,y,z in ps)
miny = min(y for x,y,z in ps)
maxy = max(y for x,y,z in ps)
minz = min(z for x,y,z in ps)
maxz = max(z for x,y,z in ps)
dirs = ((1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1))
t = 0
for x,y,z in ps:
    for dx,dy,dz in dirs:
        np = x+dx,y+dy,z+dz
        if np not in ps:
            b = True
            q = deque()
            q.append(np)
            seen = set()
            while len(q) > 0:
                p = q.popleft()

                if p in ps or p in seen:
                    continue

                px,py,pz = p
                if px < minx or px > maxx or py < miny or py > maxy or pz < minz or pz > maxz:
                    b = False
                    break

                seen.add(p)

                for pdx,pdy,pdz in dirs:
                    q.append((px+pdx, py+pdy, pz+pdz))

            if not b:
                t += 1


print(t)
