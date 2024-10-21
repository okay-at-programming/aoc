tinput = open('data').readlines()

state = tinput[0][-3:-2]
steps = int(tinput[1].split()[-2])

print(state, steps)

tape = set()
rules = {}

for i in range(3, len(tinput), 10):
    s = tinput[i][-3:-2]

    write = int(tinput[i+2][-3:-2])
    step = 1 if tinput[i+3].split()[-1].strip() == 'right.' else -1
    ns = tinput[i+4][-3:-2]

    zero = (write, step, ns)

    write = int(tinput[i+6][-3:-2])
    step = 1 if tinput[i+7].split()[-1].strip() == 'right.' else -1
    ns = tinput[i+8][-3:-2]

    one = (write, step, ns)

    rules[s] = (zero, one)

slot = 0

for i in range(steps):
    j = 1 if slot in tape else 0
    rule = rules[state][j]

    if j:
        tape.remove(slot)

    if rule[0]:
        tape.add(slot)

    slot += rule[1]

    state = rule[2]

print(len(tape))

