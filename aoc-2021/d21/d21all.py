scs = {}
for a in range(3):
    for b in range(3):
        for c in range(3):
            s = a+b+c+3
            scs[s] = scs.get(s,0) + 1

victs = []
losss = []

for ap in range(1,11):
    steps = {(ap,0):1}
    vict = {}
    loss = {}
    times = 0
    while len(steps) > 0:
        nsteps = {}
        times += 1
        for s,count in steps.items():
            pos,score = s
            for m,c in scs.items():
                npos = pos+m
                if npos > 10:
                    npos -= 10
                nscore = score+npos
                if nscore >= 21:
                    vict[times] = vict.get(times,0) + count*c
                else:
                    k = (npos,nscore)
                    nsteps[k] = nsteps.get(k,0) + count*c
                    loss[times] = loss.get(times,0) + count*c
        steps = nsteps
    victs.append(vict)
    losss.append(loss)

for a in range(1,11):
    for b in range(1,11):
        p1v,p2v = victs[a-1],victs[b-1]
        p1l,p2l = losss[a-1],losss[b-1]
        p1c,p2c = 0,0

        mi = min(min([a for a in p1v.keys()]), min([a for a in p2v.keys()]))
        ma = max(max([a for a in p1v.keys()]), max([a for a in p2v.keys()]))

        for i in range(mi,ma+1):
            p1c += p1v.get(i,0) * p2l.get(i-1,0)
            p2c += p2v.get(i,0) * p1l.get(i,0)

        print(a,b,max(p1c,p2c))
