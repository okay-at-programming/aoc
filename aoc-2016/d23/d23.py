insts = [l.strip().split() for l in open('data')]

regs = {'a':7,'b':0,'c':0,'d':0}

def get(x):
    if x in regs:
        return regs[x]
    return int(x)

def tgl(inst):
    if len(inst) == 2:
        com = 'dec' if inst[0] == 'inc' else 'inc'
    elif len(inst) == 3:
        com = 'cpy' if inst[0] == 'jnz' else 'jnz'
    return [com] + inst[1:]

i = 0
while i < len(insts):
    inst = insts[i]

    if inst[0] == 'cpy':
        regs[inst[2]] = get(inst[1])
    elif inst[0] == 'inc':
        regs[inst[1]] += 1
    elif inst[0] == 'dec':
        regs[inst[1]] -= 1
    elif inst[0] == 'jnz':
        if get(inst[1]) != 0:
            i += get(inst[2])
            continue
    elif inst[0] == 'tgl':
        j = i + get(inst[1])
        if 0 <= j < len(insts):
            insts[j] = tgl(insts[j])
    else:
        assert False

    i += 1

print(regs)

