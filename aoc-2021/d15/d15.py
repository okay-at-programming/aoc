from queue import PriorityQueue

m = [[int(x) for x in l.strip()] for l in open('data')]

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
        print(s-m[0][0] + m[end[1]][end[0]])
        break

    ns = s + m[x][y]

    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        q.put((ns,x+dx,y+dy))

