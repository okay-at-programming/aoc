data = [int(x) for x in open('data').read().strip().split(',')]

mi = min(data)
ma = max(data)

l= None

for i in range(mi, ma+1):
    t = 0
    for j in data:
        a = abs(j-i)
        t += (a*(a+1))/2
    if not l or t < l:
        l= int(t)

print(l)

