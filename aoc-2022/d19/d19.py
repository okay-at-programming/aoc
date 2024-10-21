from collections import deque

keys = ('ore','clay','obs','geo')

def use(m, ore,cl,obs,w):
    ws = set()
    ws.add(w)
    i = 0
    for r in keys:
        nore = ore - m[r][0]
        ncl = cl - m[r][1]
        nobs = obs - m[r][2]
        if nore >= 0 and ncl >= 0 and nobs >= 0:
            nw = [j for j in w]
            nw[i] += 1
            ws.update(use(m,nore,ncl,nobs,tuple(nw)))
        i += 1
    return ws

ans = 0

for l in open('data'):
    l = l.strip().split()
    m = {}
    mid = int(l[1][:-1])
    m['ore'] = int(l[6]),0,0
    m['clay'] = int(l[12]),0,0
    m['obs'] = int(l[18]),int(l[21]),0
    m['geo'] = int(l[27]),0,int(l[30])

    maxore = max([m[k][0] for k in m.keys()])

    q = deque()
    q.append((0,1,0,0,0,0,0,0,24))
    gc = 0
    seen = set()
    tt = 24
    mw = 0
    while q:
        ore,orem,cl,clm,obs,obsm,geo,geom,t = q.popleft()

        gc = max(geo,gc)

        if t == 0:
            continue

        if t < tt:
            tt = t
            print(tt, len(q), mw, gc)
            mw = 0
            seen = set()

        if orem >= maxore:
            orem = maxore
        if clm >= m['obs'][1]:
            clm = m['obs'][1]
        if obsm >= m['geo'][2]:
            obsm = m['geo'][2]
        if ore >= t*maxore - orem*(t-1):
            ore = t*maxore - orem*(t-1)
        if cl >= t*m['obs'][1] - clm*(t-1):
            cl = t*m['obs'][1] - clm*(t-1)
        if obs >= t*m['geo'][2] - obsm*(t-1):
            obs = t*m['geo'][2] - obsm*(t-1)

        k = ore,orem,cl,clm,obs,obsm,geo,geom,t
        if k in seen:
            continue
        seen.add(k)

        ways = use(m,ore,cl,obs,(0,0,0,0))
        mw = max(mw,len(ways))
        for orec, clayc, obsc, geoc in ways:
            ngeo = geo + geom
            nore = ore + orem - orec*m['ore'][0] - clayc*m['clay'][0] - obsc*m['obs'][0] - geoc*m['geo'][0]
            ncl = cl + clm - obsc*m['obs'][1]
            nobs = obs + obsm - geoc*m['geo'][2]

            q.append((nore,orem+orec, ncl, clm+clayc, nobs, obsm+obsc, ngeo, geom+geoc, t-1))


    print(mid, gc)
    print()
    ans += mid*gc
print(ans)




