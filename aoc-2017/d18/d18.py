regs = {}

def num(i):
    try:
        int(i)
    except ValueError:
        return False
    return True

def get(i):
    if num(i):
        return int(i)
    return regs.get(i, 0)

instructions = [l.strip() for l in open('data')]

l = 0

while True:
    ins = instructions[l]
    i = ins.split()[0]
    if i == 'snd':
        regs[i] = get(ins.split()[1])
    elif i == 'set':
        a = ins.split()[1]
        b = ins.split()[2]
        regs[a] = get(b)
    elif i == 'add':
        a = ins.split()[1]
        b = ins.split()[2]
        regs[a] = get(a) + get(b)
    elif i == 'mul':
        a = ins.split()[1]
        b = ins.split()[2]
        regs[a] = get(a) * get(b)
    elif i == 'mod':
        a = ins.split()[1]
        b = ins.split()[2]
        regs[a] = get(a) % get(b)
    elif i == 'rcv':
        a = ins.split()[1]
        if get(a) != 0:
            print(regs.get('snd',0))
            break
    elif i == 'jgz':
        a = ins.split()[1]
        b = ins.split()[2]
        if get(a) != 0:
            l += (get(b) - 1)
    l += 1





