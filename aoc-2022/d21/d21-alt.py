mo = {}

for l in open('data'):
    k = l.strip().split(':')[0]
    v = l.strip().split(': ')[1].split()
    mo[k] = v

step = int(1e12)
i = 0
j = 0
while True:
    j += 1
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
        print('comps:',j)
        break

    if a < b:
        print(i,a,b)
        i -= step
        step = step // 10
    else:
        i += step
