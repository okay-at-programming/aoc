x = 0

for l in open('data'):
    sig,out = l.split('|')
    sig = sig.strip().split(' ')
    m = {}
    a = {}

    for s in sig:
        k = list(s)
        k.sort()
        k = ''.join(k)
        if len(s) == 2:
            a[k] = 1
            m[1] = set(s)
        if len(s) == 3:
            a[k] = 7
            m[7]= set(s)
        if len(s) == 4:
            a[k] = 4
            m[4] = set(s)
        if len(s) == 7:
            a[k] = 8
            m[8] = set(s)

    for s in sig:
        k = list(s)
        k.sort()
        k = ''.join(k)
        if len(s) == 6:
            if len(set(s) - m[1]) == 5:
                a[k] = 6
                m[6] = set(s)
            elif len(set(s) - m[4]) == 3:
                a[k] = 0
                m[0] = set(s)
            else:
                a[k] = 9
                m[9] = set(s)

    for s in sig:
        k = list(s)
        k.sort()
        k = ''.join(k)
        if len(s) == 5:
            if len(set(s) - m[1]) == 3:
                a[k] = 3
                m[3] = set(s)
            elif len(m[6] - set(s)) == 1:
                a[k] = 5
                m[5] = set(s)
            else:
                a[k] = 2
                m[2] = set(s)

    t = 0
    for i,v in enumerate(out.strip().split(' ')):
        v = list(v)
        v.sort()
        v = ''.join(v)
        t += (10**(3-i))*a[v]
    x += t

print(x)











