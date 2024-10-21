from queue import PriorityQueue

n = [[int(x) for x in l.strip()] for l in open('data')]

m = [[None for x in range(len(n[0])*5)] for y in range(len(n)*5)]

for j in range(5):
    for i in range(5):
        for y in range(len(n)):
            for x in range(len(n[0])):
                mx = i*len(n[0]) + x
                my = j*len(n) + y
                mv = n[y][x] + i + j
                if mv > 9:
                    mv -= 9
                m[my][mx] = mv


end = len(m[0])-1,len(m)-1
q = PriorityQueue()
q.put((0,0,0))

seen = set()

while not q.empty() > 0:
    s,x,y = q.get()

    if x < 0 or x >= len(m[0]) or y < 0 or y >= len(m):
        continue

    if (x,y) in seen:
        continue
    seen.add((x,y))

    if (x,y) == end:
        r = s - m[0][0] + m[end[1]][end[0]]
        print(r)
        break

    ns = s + m[x][y]

    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        q.put((ns,x+dx,y+dy))

