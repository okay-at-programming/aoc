prog = {}

for line in open('data'):
    pn = line.split()[0].strip()
    if '>' in line:
        deps = [x.strip() for x in line.split('>')[1].strip().split(',')]
        prog[pn] = deps
    else:
        prog[pn] = []

for key in prog.keys():
    found = True
    for l in prog.values():
        if key in l:
            found = False
            break
    if found:
        print(key)
