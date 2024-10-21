lines = open('data').read()

seeds = [int(c) for c in lines.split('\n')[0].split(':')[1].split()]

print(seeds)

for mg in lines.split('\n\n')[1:]:
    maps = []
    for l in mg.split('\n')[1:]:
        l = tuple(int(c) for c in l.strip().split())
        if l:
            maps.append(l)

    ns = []
    for s in seeds:

        mapped = False
        for m in maps:
            if m[1]<=s<m[1]+m[2]:
                s = m[0] + s - m[1]
                mapped = True
                break

        ns.append(s)

    seeds = ns
    print(seeds)

print(seeds)
print(min(seeds))
