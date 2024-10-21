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

def find_adds(t,s,a,b,c):
    if t == sum(a) and t == sum(b) and t == sum(c):
        return True

    for j in range(s,len(c)):
        na = list(a)
        na.append(c[j])
        nb = list(b)
        nc = c[:j] + c[j+1:]
        if find_adds(t,j,na,nb,nc):
            return True

        na = list(a)
        nb = list(b)
        nb.append(c[j])
        nc = c[:j] + c[j+1:]
        if find_adds(t,j,na,nb,nc):
            return True

    return False



def adds(s, r):
    if sum(r) != 3*s:
        return False

    return find_adds(s,0,[],[],r)


for i in range(len(ps)):
    mq = None

    for a,r in pick(i,0,set(),ps):
        if adds(sum(a), r):
            if not mq or qe(a) < mq:
                mq = qe(a)

    if mq:
        print(i,mq)
        break
