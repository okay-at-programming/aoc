
def prep(s):
    i = 0
    r = []
    while i < len(s):
        if s[i] in '[]':
            r.append(s[i])
            i += 1
        elif s[i].isdigit():
            j = i+1
            while s[j].isdigit():
                j += 1
            r.append(int(s[i:j]))
            i = j
        else:
            i += 1
    return r

datas = [prep(s.strip()) for s in open('test6')]

def red(r):
    i = 0
    d = 0
    while i < len(r):
        if r[i] =='[':
            d += 1
            i += 1
        elif r[i] == ']':
            d -= 1
            i += 1
        elif isinstance(r[i+1],int) and d > 4:
            la = r[:i-1]
            ra = r[i+3:]
            li = len(la)-1
            ri = 0
            while li >= 0 and not isinstance(la[li],int):
                li -= 1
            while ri < len(ra) and not isinstance(ra[ri],int):
                ri += 1
            if li >= 0:
                la[li] += r[i]
                #if la[li] >= 10:
                #    la = la[:li] + ['[',la[li]//2,(la[li]+1)//2,']'] + la[li+1:]
            if ri < len(ra):
                ra[ri] += r[i+1]
                #if ra[ri] >= 10:
                #    ra = ra[:ri] + ['[',ra[ri]//2,(ra[ri]+1)//2,']'] + ra[ri+1:]

            return la + [0] + ra

        else:
            i += 1
    assert d == 0
    i = 0
    while i < len(r):
        if isinstance(r[i],int) and r[i] >= 10:
            return r[:i] + ['[',r[i]//2, (r[i]+1)//2,']'] + r[i+1:]
        i += 1
    return r

def mag(r):
    i = 0
    while i < len(r):
        if isinstance(r[i],int) and isinstance(r[i+1],int):
            return r[:i-1] + [3*r[i] + 2*r[i+1]] + r[i+3:]
        i += 1
    return r

def redit(r):
    while True:
        ar = red(r)
        if len(ar) == len(r):
            i = 0
            e = True
            while i < len(r):
                if ar[i] != r[i]:
                    e = False
                    break
                i += 1
            if e:
                break
        r = ar
    return r

def magit(r):
    while len(r) > 1:
        r = mag(r)

    return r[0]

mv = 0

for i in range(len(datas)):
    for j in range(len(datas)):
        if i == j:
            continue
        f = ['['] + datas[i] + datas[j] + [']']
        f = redit(f)
        f = magit(f)
        if f > mv:
            mv = f

print(mv)

