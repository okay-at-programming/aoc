class moon:
    def __init__(self, pos):
        self.pos = pos
        self.vel = [0,0,0]

    def update(self, other):
        for i in range(3):
            if self.pos[i] == other.pos[i]:
                continue
            self.vel[i] += 1 if self.pos[i] < other.pos[i] else -1

    def move(self):
        for i in range(3):
            self.pos[i] += self.vel[i]

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

for i in range(1000):
    for m1 in moons:
        for m2 in moons:
            m1.update(m2)

    for m1 in moons:
        m1.move()

print(sum([m.energy() for m in moons]))