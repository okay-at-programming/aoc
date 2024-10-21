regs = {}

def calc(val, sign, other):
    if sign == '>' and val > other:
        return True
    elif sign == '<' and val < other:
        return True
    elif sign == '>=' and val >= other:
        return True
    elif sign == '<=' and val <= other:
        return True
    elif sign == '==' and val == other:
        return True
    elif sign == '!=' and val != other:
        return True
    return False

m = 0

for l in open('data'):
    row = l.split()
    reg = row[0]
    mult = 1 if row[1] == 'inc' else -1
    mag = int(row[2])
    otherreg = row[4]
    other = int(row[6])

    if calc(regs.get(otherreg,0), row[5], other):
        regs[reg] = regs.get(reg,0) + mult*mag

        if regs[reg] > m:
            m = regs[reg]

print(m)
