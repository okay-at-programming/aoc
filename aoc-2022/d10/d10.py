
def cyc(c,x):
    if (c-20)%40 != 0:
        return 0
    print(c,x)
    return c * x

c = 1
x = 1
t = 0

for l in open('data'):
    l = l.strip()

    ls = l.split()
    if l == 'noop':
        t += cyc(c,x)
        c += 1
    elif ls[0] == 'addx':
        t += cyc(c,x)
        t += cyc(c+1,x)
        c += 2
        x += int(ls[1])
    else:
        print(l)
        assert False

while c <= 220:
    t += cyc(c,x)
    c += 1

print(t)
