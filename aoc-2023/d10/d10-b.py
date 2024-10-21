from collections import deque
m = [l.strip() for l in open('data')]

for y,l in enumerate(m):
    for x,c in enumerate(l):
        if c == 'S':
            p = x,y
            sp = p

def move(p, lp):
    x,y = p
    moves = []
    for dx,dy,cd in ((x+1,y, 'e'),(x,y+1,'s'),(x-1,y,'w'),(x,y-1,'n')):
        np = dx,dy
        if np == lp:
            continue
        if 0<=dx<len(m[0]) and 0<=dy<len(m):
            if cd == 'n' and m[y][x] in '|JLS' and m[dy][dx] in '|7FS':
                moves.append((dx,dy))
            if cd == 'e' and m[y][x] in '-LFS' and m[dy][dx] in '-J7S':
                moves.append((dx,dy))
            if cd == 's' and m[y][x] in '|7FS' and m[dy][dx] in '|LJS':
                moves.append((dx,dy))
            if cd == 'w' and m[y][x] in '-J7S' and m[dy][dx] in '-LFS':
                moves.append((dx,dy))

    return moves


q = deque()
q.append((p,None,0,set()))

loop = None

while q:
    p,lp,steps,path = q.popleft()

    if p == sp and lp:
        print(steps, steps//2, len(path))
        loop = path
        break

    path.add(p)

    for mo in move(p,lp):
        ns = set(path)
        q.append((mo,p,steps+1,ns))

ns = set()
sx,sy = sp
for p in ((sx+1,sy,'e'),(sx,sy+1,'s'),(sx-1,sy,'w'),(sx,sy-1,'n')):
    x,y,d = p
    p = x,y
    s = m[y][x]
    if p in loop:
        if (d == 'e' and s in '7-J') or (d == 's' and s in 'J|L') or (d == 'w' and s in 'L-F') or (d == 'n' and s in '7|F'):
            ns.add(p)

r = ''
if ns == {(sx-1,sy),(sx+1,sy)}:
    r = '-'
elif ns == {(sx-1,sy),(sx,sy-1)}:
    r = 'J'
elif ns == {(sx-1,sy),(sx,sy+1)}:
    r = '7'
elif ns == {(sx,sy-1),(sx+1,sy)}:
    r = 'L'
elif ns == {(sx,sy-1),(sx,sy+1)}:
    r = '|'
elif ns == {(sx+1,sy),(sx,sy+1)}:
    r = 'F'
else:
    assert False

m[sy] = m[sy][:sx] + r + m[sy][sx+1:]

for l in m:
    print(l)



def look(p):
    if p in loop:
        return False

    cc = 0
    x,y = p
    crossing = ''
    l = 0
    while x >= 0:
        s = m[y][x]
        if crossing == 'l':
            if s == 'F':
                cc += 1
                crossing = ''
            elif s == 'L':
                crossing = ''
            elif s == '-':
                l += 1
            else:
                assert False
        elif crossing == 'r':
            if s == 'L':
                cc += 1
                crossing = ''
            elif s == 'F':
                crossing = ''
            elif s == '-':
                l += 1
            else:
                assert False
        elif (x,y) in loop:
            if s == '|':
                cc += 1
            elif s == '7':
                crossing = 'r'
            elif s == 'J':
                crossing = 'l'
            else:
                assert False

        x -= 1
    return cc%2 == 1

y = 0
inside = set()
outside = set()

while y < len(m):
    x = 0
    while x < len(m[0]):

        p = x,y

        if look(p):
            print(p)
            inside.add(p)

        x += 1
    y += 1

print(len(inside))
