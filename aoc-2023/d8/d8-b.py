lines = open('data').read()

insts,moves = lines.split('\n\n')

m = {}
ks = []
for l in moves.strip().split('\n'):
    k = l.split()[0]
    lef = l.split()[2][1:-1]
    rig = l.split()[3][:-1]

    m[k] = (lef, rig)
    if k.endswith('A'):
        ks.append(k)

def get_count(k):
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

        if k.endswith('Z'):
            return steps

ls = []
for k in ks:
    c = get_count(k)
    ls.append(c)

lcm = ls[0]

for e in ls[1:]:
    num1 = lcm
    num2 = e
    gcd = 1
    while num2 != 0:
        t = num2
        num2 = num1 % num2
        num1 = t
    gcd = num1
    lcm = (lcm * e) // gcd

print(lcm)
