regs = {
    'b':79,
    'c':79,
    'd':0,
    'e':0,
    'f':0,
    'g':0,
    'h':0
}

regs['b'] = regs['b']*100 + 100000
regs['c'] = regs['b'] + 17000

while True:
    regs['f'] = 1
    regs['d'] = 2

    d = regs['d']

    while d*d < regs['b']:
        if regs['b'] % d == 0:
            regs['f'] = 0
            break
        d += 1

    if regs['f'] == 0:
        regs['h'] += 1

    regs['g'] = regs['b'] - regs['c']
    regs['b'] += 17

    print(regs)

    if regs['g'] == 0:
        break

print(regs)


