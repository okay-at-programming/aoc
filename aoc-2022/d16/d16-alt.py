from collections import deque

ts = {}

for l in open('data'):
    k = l.split()[1]
    r = int(l.split('=')[1].split(';')[0])
    to = tuple(''.join(l.split()[9:]).split(','))
    ts[k] = (r,to)

q = deque()
q.append(('AA', 'AA', 26, 0,[]))
seen = set()
m = 0
while q:
    k,ek,t,cr,co = q.popleft()

    if t>= 0:
        if cr > m:
            print(cr)
        m = max(cr, m)

    if t <= 0 or len(ts) == len(co):
        continue

    if (k,ek,cr) in seen:
        continue
    seen.add((k,ek,cr))

    r,to = ts[k]
    er,eto = ts[ek]

    if k not in co:
        crn = cr + (t-1)*r
        con = list(co)
        con.append(k)

        if ek not in con and er > 0:
            crnn = crn + (t-1)*er
            conn = list(con)
            conn.append(ek)
            q.append((k,ek,t-1,crnn, conn))

        if r > 0:
            for eok in eto:
                q.append((k, eok, t-1, crn, list(con)))

    for ok in to:
        if ek not in co and er > 0:
            crn = cr + (t-1)*er
            con = list(co)
            con.append(ek)
            q.append((ok, ek, t-1, crn, con))

        for eok in eto:
            q.append((ok, eok, t-1, cr, list(co)))

print(m)
