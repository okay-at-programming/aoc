
def comp(i, a, b, c, r):
    if i == 'addr':
        r[c] = r[a] + r[b]
    elif i == 'addi':
        r[c] = r[a] + b
    elif i == 'mulr':
        r[c] = r[a] * r[b]
    elif i == 'muli':
        r[c] = r[a] * b
    elif i == 'banr':
        r[c] = r[a] & r[b]
    elif i == 'bani':
        r[c] = r[a] & b
    elif i == 'borr':
        r[c] = r[a] | r[b]
    elif i == 'bori':
        r[c] = r[a] | b
    elif i == 'setr':
        r[c] = r[a]
    elif i == 'seti':
        r[c] = a
    elif i == 'gtir':
        r[c] = 1 if a > r[b] else 0
    elif i == 'gtri':
        r[c] = 1 if r[a] > b else 0
    elif i == 'gtrr':
        r[c] = 1 if r[a] > r[b] else 0
    elif i == 'eqir':
        r[c] = 1 if a == r[b] else 0
    elif i == 'eqri':
        r[c] = 1 if r[a] == b else 0
    elif i == 'eqrr':
        r[c] = 1 if r[a] == r[b] else 0
    else:
        print('error')

fn = 'data'
bind = int(open(fn).readlines()[0].split()[1])
ip = 0

instr = []
for i in open(fn).readlines()[1:]:
    s = i.strip().split()
    instr.append((s[0], int(s[1]), int(s[2]), int(s[3])))
    print(len(instr)-1,(s[0], int(s[1]), int(s[2]), int(s[3])))

reg = [3909249,0,0,0,0,0]
ip = 0

while ip < len(instr):
    reg[bind] = ip

    i = instr[ip]
    comp(i[0], i[1], i[2], i[3], reg)
    if ip == 28:
        print(ip, i, reg)

    ip = reg[bind]
    ip += 1



