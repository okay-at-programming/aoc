regs = {'a':0, 'b':0, 'c':0,'d':0}
insts = open('data').readlines()

def get(s):
    if s in regs:
        return regs[s]
    return int(s)

i = 0
while i < len(insts):
    ls = insts[i].split()

    if ls[0] == 'cpy':
        regs[ls[2]] = get(ls[1])
        i += 1
    elif ls[0] == 'inc':
        regs[ls[1]] += 1
        i += 1
    elif ls[0] == 'dec':
        regs[ls[1]] -= 1
        i += 1
    elif ls[0] == 'jnz':
        if get(ls[1]) != 0:
            i += get(ls[2])
        else:
            i += 1
    else:
        assert False

print(regs)
