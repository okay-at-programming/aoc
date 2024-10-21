from collections import deque

target = 31,39
fn = 1350
grid = {}

def iswall(x,y):
    w = grid.get((x,y))
    if w in (True, False):
        return w
    a = x*x + 3*x + 2*x*y + y + y*y + fn
    c = bin(a).count('1')
    r = False
    if c%2 == 1:
        r = True
    grid[(x,y)] = r
    return r

q = deque()
q.append((1,1,0, []))
seen = set()

while len(q) > 0:
    x,y,steps,path = q.popleft()

    p = x,y

    if p == target:
        print(steps)
        break

    if p in seen or x < 0 or y < 0:
        continue

    if iswall(x,y):
        continue

    seen.add(p)

    path.append(p)
    for dx,dy in ((0,1),(1,0),(0,-1),(-1,0)):
        npath = path[:]
        q.append((x+dx,y+dy,steps+1,npath))


