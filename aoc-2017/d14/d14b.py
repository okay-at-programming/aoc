test = 'flqrgnkx'
data = 'hfdlxzhv'
#data = test

def rev(l, s, d):
    for i in range(d//2):
        i1 = (s+i)%len(l)
        i2 = (s+d-i-1)%len(l)
        l[i1],l[i2] = l[i2],l[i1]

def dh(l):
    a = l[0]
    for b in l[1:]:
        a = a^b
    return a

def hash(s):
    data = [ord(c) for c in s]
    data.extend([17, 31, 73, 47, 23])

    arr = [x for x in range(256)]
    i = 0
    ss = 0

    for _ in range(64):
        for l in data:
            rev(arr,i,l)
            i = (i+l+ss)%len(arr)
            ss += 1

    denseh = [dh(arr[j:j+16]) for j in range(0,256,16)]

    output = ''

    for c in denseh:
        output += "{0:08b}".format(c)

    return output

grid = []
for i in range(128):
    s = data + '-' + str(i)

    h = hash(s)

    grid.append(h)

regions = set()

for i in range(128):
    for j in range(128):
        if grid[i][j] == '0':
            continue

        seen = set()
        q = [(i,j)]
        lp = i,j
        while len(q) > 0:
            p = q.pop(0)

            if p in regions:
                lp = None
                break

            if p in seen or grid[p[0]][p[1]] == '0':
                continue
            seen.add(p)

            for di,dj in ((0,1),(1,0),(0,-1),(-1,0)):
                np = p[0]+di,p[1]+dj
                if np[0] < 128 and np[0] >= 0 and np[1] < 128 and np[1] >= 0:
                    q.append(np)
        if lp:
            regions.add(lp)

print(len(regions))

