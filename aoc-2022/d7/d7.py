up = {}
dirs = {}
cd = []

for l in open('data'):
    l = l.strip().split()

    if l[1] == 'cd':
        if l[2] == '..':
            cd.pop(-1)
        else:
            cd.append(l[2])
    elif l[1] == 'ls':
        dirs[''.join(cd)] = {'total':0,'dirs':[]}
    elif l[0] == 'dir':
        p = ''.join(cd)
        dirs[''.join(cd)]['dirs'].append(p+l[1])
    elif l[0].isnumeric():
        dirs[''.join(cd)]['total'] += int(l[0])
    else:
        assert False

print(up)
print(dirs)

sizes = {}

while len(sizes) < len(dirs):

    for k in dirs.keys():
        if k in sizes:
            continue

        ts = dirs[k]['total']
        inc = False

        for o in dirs[k]['dirs']:
            if o in sizes:
                ts += sizes[o]
            else:
                inc = True

        if inc:
            continue

        sizes[k] = ts

print(sizes)
t = 0
for k,v in sizes.items():
    if v <= 100000:
        t += v

print(t)
