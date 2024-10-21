mo = {}

for l in open('data'):
    k = l.strip().split(':')[0]
    v = l.strip().split(': ')[1].split()
    mo[k] = v

inc = True
prev = 1e12
i = 0
while True:
    op = True
    m = {k:v for k,v in mo.items()}
    m['humn'] = i
    while op:

        op = False

        for k,v in m.items():
            if k == 'root':
                continue
            elif isinstance(v,int):
                continue
            elif len(v) == 1:
                m[k] = int(v[0])
                op = True
            elif len(v) == 3 and isinstance(m[v[0]], int) and isinstance(m[v[2]], int):
                a,e,b = int(m[v[0]]),v[1],int(m[v[2]])
                if e == '+':
                    r = a + b
                elif e == '-':
                    r =  a-b
                elif e == '*':
                    r = a*b
                elif e == '/':
                    r = a//b
                m[k] = r
                op = True

    a,b = int(m[m['root'][0]]),int(m[m['root'][2]])

    if a == b:
        print(i)
        break
    d = abs(a-b)

    if d < prev:
        if inc:
            if d > 10000000000000000:
                i += 10000000000
            elif d > 100000000000000:
                i += 1000000000
            elif d > 1000000000000:
                i += 100000000
            elif d > 10000000000:
                i += 1000000
            elif d > 100000000:
                i += 100000
            elif d > 1000000:
                i += 1000
            elif d > 1000:
                i += 100
            else:
                i += 1
        else:
            i -= 1
    elif d == prev:
        if inc:
            i += 1
        else:
            i -= 1
    else:
        inc = not inc
    prev = d

    print(i,a,b)
