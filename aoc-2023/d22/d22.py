bs = []
n = ord('A')
for l in open('data'):
    s,e = l.strip().split('~')
    s = [int(x) for x in s.split(',')]
    e = [int(x) for x in e.split(',')]
    p = [[s[i],e[i]] for i in range(3)]
    p.append(chr(n))
    bs.append(p)
    n += 1

def lowest(bs,sj):
    i = -1
    ilp = None
    j = sj
    for b in bs[sj:]:
        lp = min(b[2])
        if not ilp or lp < ilp:
            ilp = lp
            i = j
        j += 1
    return i

def clear(i,bs,ig,af):
    tb = bs[i]
    dd = 1
    if min(tb[2]) == 1:
        return 0
    for j,ob in enumerate(bs[:i]):
        if i == j or j in ig:
            continue
        wb = False
        if (af and max(ob[2]) < min(tb[2])) or (not af and max(ob[2]) + 1 == min(tb[2])):
            if (ob[0][0]<=tb[0][0]<=ob[0][1] or ob[0][0]<=tb[0][1]<=ob[0][1]):
                if (ob[1][0]<=tb[1][0]<=ob[1][1] or ob[1][0]<=tb[1][1]<=ob[1][1]):
                    wb = True
                    if not af:
                        return False
                if (tb[1][0]<=ob[1][0]<=tb[1][1] or tb[1][0]<=ob[1][1]<=tb[1][1]):
                    wb = True
                    if not af:
                        return False
            if (tb[0][0]<=ob[0][0]<=tb[0][1] or tb[0][0]<=ob[0][1]<=tb[0][1]):
                if (ob[1][0]<=tb[1][0]<=ob[1][1] or ob[1][0]<=tb[1][1]<=ob[1][1]):
                    wb = True
                    if not af:
                        return False
                if (tb[1][0]<=ob[1][0]<=tb[1][1] or tb[1][0]<=ob[1][1]<=tb[1][1]):
                    wb = True
                    if not af:
                        return False
        if wb:
            if max(ob[2]) >= dd:
                dd = max(ob[2])+1
    if not af:
        return True
    return min(tb[2])-dd


print('sorting')
i = 0
while i < len(bs):
    li = lowest(bs,i)
    if li != i:
        lb = bs.pop(li)
        bs.insert(i,lb)
    i += 1

print('dropping')
for i,b in enumerate(bs):
    dd = clear(i,bs,[],True)
    b[2][0] -= dd
    b[2][1] -= dd

print('sorting')
i = 0
while i < len(bs):
    li = lowest(bs,i)
    if li != i:
        lb = bs.pop(li)
        bs.insert(i,lb)
    i += 1

def printout():
    minx = min(min(b[0]) for b in bs)
    maxx = max(max(b[0]) for b in bs)
    miny = min(min(b[1]) for b in bs)
    maxy = max(max(b[1]) for b in bs)
    minz = min(min(b[2]) for b in bs)
    maxz = max(max(b[2]) for b in bs)

    print('x')
    for z in range(maxz,minz-1,-1):
        s = ''
        for x in range(minx,maxx+1):
            c = set()
            for b in bs:
                if b[2][0]<=z<=b[2][1] and b[0][0]<=x<=b[0][1]:
                    c.add(b[3])
            if len(c) == 0:
                s += '.'
            elif len(c) == 1:
                s += c.pop()
            else:
                s += '?'
        print(s,z)
    print()
    print('y')
    for z in range(maxz,minz-1,-1):
        s = ''
        for y in range(miny,maxy+1):
            c = set()
            for b in bs:
                if b[2][0]<=z<=b[2][1] and b[1][0]<=y<=b[1][1]:
                    c.add(b[3])
            if len(c) == 0:
                s += '.'
            elif len(c) == 1:
                s += c.pop()
            else:
                s += '?'
        print(s,z)

    print()


c = 0
for i,tb in enumerate(bs):
    print('disintergrating',tb[3])
    p = True
    j = i+1
    for ob in bs[i+1:]:
        if clear(j,bs,[i],False):
            p = False
            break
        if min(ob[2]) > max(tb[2]) + 1:
            break
        j += 1
    if p:
        print(i,tb)
        c += 1

print(c)
