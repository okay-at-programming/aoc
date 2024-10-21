m = {}

for l in open('data'):
    k = l.strip().split(':')[0]
    v = l.strip().split(': ')[1].split()
    m[k] = v

op = True

while op:

    op = False

    for k,v in m.items():
        if isinstance(v,int):
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

print(m)
print(m['root'])
