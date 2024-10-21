lines = open('data').read()

seeds = [int(c) for c in lines.split('\n')[0].split(':')[1].split()]

print(seeds)
x = 0
ranges = []
while x < len(seeds):
    ranges.append((seeds[x], seeds[x] + seeds[x+1]))
    x += 2
print(ranges)

for mg in lines.split('\n\n')[1:]:
    maps = []
    print(mg.split('\n')[0])
    for l in mg.split('\n')[1:]:
        l = tuple(int(c) for c in l.strip().split())
        if l:
            maps.append(l)

    ns = []
    x = 0
    while x < len(ranges):
        r = ranges[x]
        md = False
        for m in maps:

            r1 = r[0],max(r[0],m[1])
            r2 = max(r[0],m[1]),min(r[1],m[1]+m[2])
            r3 = min(r[1],m[1]+m[2]),r[1]
            if r2[0] < r2[1]:
                ns.append((r2[0] + m[0] - m[1], r2[1] + m[0] - m[1]))
                md = True
                if r1[0] < r1[1]:
                    ranges.append(r1)
                if r3[0] < r3[1]:
                    ranges.append(r3)
        if not md:
            ns.append(r)
        x += 1

    ranges = ns

print()
print(min([x for x,y in ranges]))
