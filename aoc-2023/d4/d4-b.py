cps = {1:1}
x = 1
for l in open('data'):
    w = l.split(':')[1].split('|')[0].strip().split()
    y = l.split(':')[1].split('|')[1].strip().split()

    w = set(map(int, w))
    y = set(map(int, y))

    s = w.intersection(y)

    if x not in cps:
        cps[x] = 1

    for y in range(x+1, x+1+len(s)):
        cps[y] = cps.get(y,1) + cps.get(x,1)

    print(cps)
    x += 1

print(x)
print(cps)
print(sum([v for k,v in cps.items() if k < x]))
