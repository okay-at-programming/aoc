instr = [l.strip() for l in open('data')]


def get(reg, val):
    try:
        return int(val)
    except ValueError:
        return reg.get(val,0)

i= 0
regs = {'a':1}
t = 0

while t < 100 and i < len(instr):
    t += 1

    ins, x, y = instr[i].split()
    print(i, regs)

    if ins == 'set':
        regs[x] = get(regs,y)
    elif ins == 'sub':
        regs[x] = get(regs,x) - get(regs,y)
    elif ins == 'mul':
        regs[x] = get(regs,x)*get(regs,y)
    elif ins == 'jnz':
        if get(regs,x) != 0:
            i += (get(regs,y) -1)

    i += 1

