insts = [l.strip() for l in open('data')]

regs = {'a':1,'b':0}

i = 0
while i < len(insts):
    inst = insts[i].split()

    if inst[0] == 'hlf':
        regs[inst[1]] //= 2
    elif inst[0] == 'tpl':
        regs[inst[1]] *= 3
    elif inst[0] == 'inc':
        regs[inst[1]] += 1
    elif inst[0] == 'jmp':
        i += int(inst[1])
        continue
    elif inst[0] == 'jie':
        if regs[inst[1][:-1]]%2 == 0:
            i += int(inst[2])
            continue
    elif inst[0] == 'jio':
        if regs[inst[1][:-1]] == 1:
            i += int(inst[2])
            continue
    else:
        assert False

    i += 1

print(regs)
