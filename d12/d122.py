class moon:
    def __init__(self, pos):
        self.pos = pos
        self.vel = [0,0,0]

    def update(self, other, i):
        if self.pos[i] == other.pos[i]:
            return
        self.vel[i] += 1 if self.pos[i] < other.pos[i] else -1

    def move(self, i):
        self.pos[i] += self.vel[i]

    def state(self, i):
        return str(self.pos[i]) + ' ' + str(self.vel[i]) + ' '

    def energy(self):
        return sum([abs(i) for i in self.pos]) * sum([abs(i) for i in self.vel])

    def __str__(self):
        return str(self.pos) + ' - ' + str(self.vel)


moons = []
for line in open('data','r'):
    vals = line.split()
    x = int(vals[0][3:-1])
    y = int(vals[1][2:-1])
    z = int(vals[2][2:-1])
    moons.append(moon([x,y,z]))

loops = []
for i in range(3):
    it = 0
    states = set()
    while True:
        s = ''
        for m1 in moons:
            for m2 in moons:
                m1.update(m2, i)

        for m1 in moons:
            m1.move(i)
            s += m1.state(i)

        if s in states:
            break

        states.add(s)
        it += 1

    print(i, it)
    loops.append(it)

def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a

def lcm(a,b):
    return int(a*b/gcd(a,b))

a = lcm(loops[0],loops[1])
print(lcm(loops[2], a))
