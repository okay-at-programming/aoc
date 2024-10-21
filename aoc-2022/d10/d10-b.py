
def cyc(m,c,x):
    r = (c-1)//40
    c = (c-1)%40
    if x-1<=c<=x+1:
        m.add((r,c))

c = 1
x = 1
m = set()

for l in open('data'):
    l = l.strip()

    ls = l.split()
    if l == 'noop':
        cyc(m,c,x)
        c += 1
    elif ls[0] == 'addx':
        cyc(m,c,x)
        cyc(m,c+1,x)
        c += 2
        x += int(ls[1])
    else:
        print(l)
        assert False

for r in range(6):
    s = ''
    for c in range(40):
        if (r,c) in m:
            s += '#'
        else:
            s += ' '
    print(s)
