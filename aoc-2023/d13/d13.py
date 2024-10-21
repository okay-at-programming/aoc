

def refc(x,y,mc,l):
    if x < mc:
        nx = mc + (mc-x) - 1
        if 0<=nx<l:
            return nx
        return None

    nx = mc - (x-mc) - 1
    if 0<=nx<l:
        return nx
    return None

def refr(x,y,mr,l):
    if y < mr:
        ny = mr + (mr-y) - 1
        if 0<=ny<l:
            return ny
        return None
    ny = mr - (y-mr) - 1
    if 0<=ny<l:
        return ny
    return None


def f(b):

    for mc in range(1,len(b[0])):
        v = True
        for y,r in enumerate(b):
            for x,c in enumerate(r):
                mx = refc(x,y,mc,len(b[0]))
                if mx:
                    m = b[y][mx]
                    if m != c:
                        v = False
        if v:
            return mc

    for mr in range(1,len(b)):
        v = True
        for y,r in enumerate(b):
            for x,c in enumerate(r):
                my = refr(x,y,mr,len(b))
                if my:
                    m = b[my][x]
                    if m != c:
                        v = False
        if v:
            return 100*mr




blocks = open('data').read().split('\n\n')
t = 0
for b in blocks:

    b = [l.strip() for l in b.split('\n') if l]
    s = f(b)
    t += s

print(t)

