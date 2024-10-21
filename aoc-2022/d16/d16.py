from collections import deque

ts = {}

for l in open('data'):
    k = l.split()[1]
    r = int(l.split('=')[1].split(';')[0])
    to = tuple(''.join(l.split()[9:]).split(','))
    ts[k] = (r,to)

q = deque()
q.append(('AA',30, 0,[]))
seen = set()
m = 0
while q:
    k,t,cr,co = q.popleft()

    if t>= 0:
        m = max(cr, m)

    if t <= 0 or len(ts) == len(co):
        continue

    if (k,cr) in seen:
        continue
    seen.add((k,cr))

    r,to = ts[k]

    if k not in co:
        crn = cr + (t-1)*r
        con = list(co)
        con.append(k)
        q.append((k,t-1,crn,con))

    for ok in to:
        q.append((ok, t-1, cr, list(co)))

print(m)
