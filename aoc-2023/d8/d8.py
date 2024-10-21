lines = open('data').read()

insts,moves = lines.split('\n\n')

m = {}

for l in moves.strip().split('\n'):
    k = l.split()[0]
    lef = l.split()[2][1:-1]
    rig = l.split()[3][:-1]

    m[k] = (lef, rig)

k = 'AAA'
i = 0
steps = 0
while True:

    if insts[i] == 'L':
        k = m[k][0]
    elif insts[i] == 'R':
        k = m[k][1]
    else:
        assert False

    i = (i+1)%len(insts)
    steps += 1

    if k == 'ZZZ':
        print(steps)
        break

