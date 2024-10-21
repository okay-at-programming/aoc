data = [int(x) for x in open('data').read().strip().split(',')]

mi = min(data)
ma = max(data)

l= None

for i in range(mi, ma+1):
    t = 0
    for j in data:
        t += abs(j-i)
    if not l or t < l:
        l= t

print(l)

