ps = [int(x) for x in open('data')]

def qe(l):
    p = 1
    for x in l:
        p *= x
    return p

def pick(i, s, p, ps):
    if len(p) == i:
        return [(p,ps)]

    r = []
    for j in range(s,len(ps)):
        np = set(p)
        np.add(ps[j])
        nps = ps[:j] + ps[j+1:]
        r.extend(pick(i,j,np,nps))
    return r

def find_adds(s,a,b):
    if sum(a) == sum(b):
        return True

    for j in range(s,len(b)):
        na = list(a)
        na.append(b[j])
        nb = b[:j] + b[j+1:]
        if find_adds(j,na,nb):
            return True
    return False



def adds(s, r):
    if sum(r) != 2*s:
        return False

    return find_adds(0,[],r)


for i in range(len(ps)):
    mq = None

    for a,r in pick(i,0,set(),ps):
        if adds(sum(a), r):
            if not mq or qe(a) < mq:
                mq = qe(a)

    if mq:
        print(i,mq)
        break
