from collections import deque
g = {}

mx = 0
my = 0
for y,l in enumerate(open('data')):
    for x,c in enumerate(l.strip()):
        if c in '#<>^v':
            g[(x,y)] = c
        mx = max(x,mx)
        my = max(y,my)

mx += 1
my += 1

for x in range(mx):
    if (x,0) not in g:
        s = x,0
    if (x,my-1) not in g:
        e = x,my-1

print(s,e)
q = deque()
q.append((s,set()))

while q:
    p,seen = q.popleft()

    if p == e:
        print(len(seen))
        continue

    if p in seen:
        continue

    seen.add(p)
    x,y = p

    for dx,dy,d in ((x+1,y,'>'),(x,y+1,'v'),(x-1,y,'<'),(x,y-1,'^')):
        if 0<=dx<mx and 0<=dy<my:
            c = g.get((dx,dy),'')
            if c == '#':
                continue
            if not c or c == d:
                ns = set(seen)
                q.append(((dx,dy),ns))


