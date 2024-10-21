data = open('data', 'r').read().split("\n")

class pot:
    def __init__(self, index, state):
        self.index = index
        self.state = state
        self.next = '.'

    def __str__(self):
        return self.state

    def nextstate(self):
        self.state = self.next
        self.next = '.'

    def value(self):
        return self.index if self.state == '#' else 0


state = []
for i, s in enumerate(data[0][15:]):
    p = pot(i, s)
    state.append(p)

lines = data[2:-1]

rules = {}
for line in lines:
    rules[line[:5]] = line[-1:]

prev = -1
pred = 0
diff = -1
i = 0
while pred != diff:

    start = state[0].index-1
    end = state[-1].index+1
    addstart = False
    addend = False
    for j in range(5):
        if state[j].state == '#':
            addstart = True
        if state[-j].state == '#':
            addend = True

    for j in range(5):
        if addstart:
            p1 = pot(start-j, '.')
            state.insert(0, p1)
        if addend:
            p2 = pot(end+j, '.')
            state.append(p2)

    for j, p in enumerate(state):
        comp = ''
        comp += '.' if j-2 < 0 else state[j-2].state
        comp += '.' if j-1 < 0 else state[j-1].state
        comp += p.state
        comp += '.' if j+1 >= len(state) else state[j+1].state
        comp += '.' if j+2 >= len(state) else state[j+2].state

        if comp in rules:
            p.next = rules[comp]

    total = 0
    for p in state:
        total += p.value()
        p.nextstate()

    pred = diff
    diff = total - prev

    print(i, total, diff, pred)
    i += 1
    prev = total

a = (50000000001 - i)*diff
total += a

print(total)

