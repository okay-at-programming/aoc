insts = [l.strip() for l in open('test2')]

regs = {'a':0,'b':0,'c':0,'d':0}

def get(x):
    if x in regs:
        return regs[x]
    return int(x)

i = 0
while i < len(insts):
    inst = insts[i].split()

    if inst[0] == 'cpy':
        regs[inst[2]] = get(inst[1])
    elif inst[0] == 'inc':
        regs[inst[1]] += 1
    elif inst[0] == 'dec':
        regs[inst[1]] -= 1
    elif inst[0] == 'jnz':
        if get(inst[1]) != 0:
            i += int(inst[2])
            continue
    else:
        assert False

    i += 1

print(regs)

