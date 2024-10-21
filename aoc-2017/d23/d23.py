instr = [l.strip() for l in open('data')]


def get(reg, val):
    try:
        return int(val)
    except ValueError:
        return reg.get(val,0)

i= 0
regs = {}
c = 0

while i < len(instr):

    ins, x, y = instr[i].split()
    print(i, regs)

    if ins == 'set':
        regs[x] = get(regs,y)
    elif ins == 'sub':
        regs[x] = get(regs,x) - get(regs,y)
    elif ins == 'mul':
        c += 1
        regs[x] = get(regs,x)*get(regs,y)
    elif ins == 'jnz':
        if get(regs,x) != 0:
            i += (get(regs,y) -1)

    i += 1

print(c)
