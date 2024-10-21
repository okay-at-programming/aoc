from collections import deque
from time import time
import sys

filename = 'data.txt'
if len(sys.argv) > 1:
    filename = sys.argv[1]

f = [l.strip() for l in open(filename)]
start = time()

cave = []
units = {}

class unit:
    def __init__(self, t, p):
        self.type = t
        self.pos = p
        self.done = False
        self.ap = 3
        self.hp = 200

    def move(self):
        if isOpen(self.type, self.pos):
            return self.pos

        seen = set()
        seen.add(self.pos)
        moves = deque()
        for n in neighbours(self.pos):
            moves.append((n, 1, n))
        possteps = -1
        poss= None

        while len(moves) > 0:
            m = moves.popleft()
            s = m[0]
            if s in seen:
                continue
            if cave[s[1]][s[0]] == '#' or s in units:
                continue
            if possteps > 0 and m[1] > possteps:
                break
            if isOpen(self.type, s):
                if possteps == -1:
                    possteps = m[1]
                    poss = m[2],s
                elif s == poss[1]:
                    if isBefore(m[2], poss[0]):
                        poss = m[2],s
                elif isBefore(s, poss[1]):
                    poss = m[2],s
                continue

            seen.add(s)

            for n in neighbours(s):
                moves.append((n, m[1]+1, m[2]))

        if poss:
            self.pos = poss[0]

        return self.pos

    def attack(self):
        target = None
        for d in neighbours(self.pos):
            if d in units and units[d].type != self.type:
                if not target or units[d].hp < target.hp:
                    target = units[d]

        if not target:
            return

        target.hp -= self.ap

        if target.hp <= 0:
            return target.pos

        return None

def isBefore(t, o):
    if t[1] < o[1]:
        return True
    if t[1] == o[1] and t[0] < o[0]:
        return True
    return False

def isOpen(t, o):
    for d in neighbours(o):
       if d in units and units[d].type != t:
            return True
    return False

def neighbours(p):
    n = []
    for d in (0,-1), (-1,0), (1,0), (0,1):
        n.append((p[0] + d[0], p[1] + d[1]))
    return n

def printout():
    y = 0
    while y < len(cave):
        x = 0
        l = ''
        hs = []
        while x < len(cave[y]):
            if (x,y) in units:
                u = units[(x,y)]
                l += u.type
                hs.append(u.type + '(' + str(u.hp) + ')')
            else:
                l += cave[y][x]
            x += 1
        print(l + '    ' + ','.join(hs))
        y += 1
    print(time() - start)
    print()

def enemycount(t):
    c = 0
    for u in units.values():
        if u.type != t:
            c += 1
    return c

y = 0
masterunits = {}

while y < len(f):
    r = ""
    x = 0
    while x < len(f[y]):
        if f[y][x] == '#' or f[y][x] == '.':
            r += f[y][x]
        else:
            r += '.'
            masterunits[(x,y)] = unit(f[y][x], (x,y))
        x += 1
    cave.append(r)
    y += 1



power = 3

while True:
    printout()
    i = 1

    elveswin = True

    units = {}
    for u in masterunits.values():
        nu = unit(u.type, u.pos)
        if nu.type == 'E':
            nu.ap = power
        units[nu.pos] = nu

    while elveswin:
        print('ap:', power, 'round:', i)
        y = 0
        enemies = True
        unitcount = len(units)
        while y < len(cave) and enemies and elveswin:
            x = 0
            while x < len(cave[y]) and enemies and elveswin:
                if (x,y) in units and not units[(x,y)].done:
                    un= units.pop((x,y))
                    np = un.move()
                    un.done = True
                    units[np] = un

                    t = un.attack()

                    if t:
                        dead = units.pop(t)
                        if dead.type == 'E':
                            elveswin = False
                    unitcount -= 1

                    if enemycount(un.type) == 0 and unitcount > 0:
                        enemies = False

                x += 1
            y += 1

        for u in units.values():
            u.done = False

        types = {}
        for u in units.values():
            if u.type not in types:
                types[u.type] = 0
            types[u.type] += u.hp

        if len(types) == 1:
            if not enemies:
                i -= 1
            for hp in types.values():
                print(hp, ' x ', i, ' = ', hp*i)
            break

        i += 1


        printout()
    if elveswin:
        print(power)
        break
    power += 1

