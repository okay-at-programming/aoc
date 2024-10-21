scanners = []

for l in open('data'):
    l = l.strip()
    if not l:
        continue

    if 'scanner' in l:
        scanners.append(set())
        continue

    x,y,z = [int(x) for x in l.split(',')]

    scanners[-1].add((x,y,z))

def rotate(x,y,z,i):
    r = [(x, y, z) ,(x,-z, y) ,(x,-y,-z) ,(x, z,-y)
        ,(y, z, x) ,(y,-x, z) ,(y,-z,-x) ,(y, x,-z)
        ,(z, x, y) ,(z,-y, x) ,(z,-x,-y) ,(z, y,-x)
        ,(-z,-y,-x) ,(-z, x,-y) ,(-z, y, x) ,(-z,-x, y)
        ,(-y,-x,-z) ,(-y, z,-x) ,(-y, x, z) ,(-y,-z, x)
        ,(-x,-z,-y) ,(-x, y,-z) ,(-x, z, y) ,(-x,-y, z)]

    return r[i]

def commonpoints(m,leftmap):

    for r in range(24):

        for a in leftmap:
            for b in m:
                rot = rotate(a[0],a[1],a[2],r)
                of = (b[0]-rot[0],b[1]-rot[1],b[2]-rot[2])
                cps = set()
                for na in leftmap:
                    na = rotate(na[0],na[1],na[2],r)
                    na = of[0]+na[0],of[1]+na[1],of[2]+na[2]
                    cps.add(na)

                if len(cps & m) >= 12:
                    return cps,of
    return None,None

def man(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(a[2]-b[2])

maps = scanners[:1]
fullmap = scanners[0]
left = scanners[1:]
scanners = []
scanners.append((0,0,0))

mstart = 0
istart = 0
while len(left) > 0:
    done = False
    for j in range(mstart,len(maps)):
        for i in range(istart,len(left)):
            cp,scan = commonpoints(maps[j],left[i])

            if cp:
                fullmap.update(cp)
                scanners.append(scan)
                maps.append(cp)
                left = left[:i] + left[i+1:]
                done = True
                print(len(maps),len(left))
                istart = i
                mstart = j
                break
        if done:
            break
        istart = 0
    print('loop',mstart,istart)

print(len(fullmap))
top = 0
for i in range(len(scanners)):
    for j in range(i+1,len(scanners)):
        d = man(scanners[i],scanners[j])
        if d > top:
            top = d

print(top)

