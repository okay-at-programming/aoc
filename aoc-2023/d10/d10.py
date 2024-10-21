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
q.append((p,None,0))

while q:
    p,lp,steps = q.popleft()

    if p == sp and lp:
        print(steps, steps//2)
        continue

    for mo in move(p,lp):
        q.append((mo,p,steps+1))


