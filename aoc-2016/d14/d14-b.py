from hashlib import md5

quints = {}
trips = {}

def process(i):
    s = f'qzyelonm{i}'.encode()
    m = md5(s)
    for _ in range(2016):
        m = md5(m.hexdigest().encode())

    m = m.hexdigest()

    ts = None
    qs = set()

    for j in range(len(m)-2):
        if m[j] == m[j+1] and m[j] == m[j+2]:
            if not ts:
                ts = m[j]
            if j + 4 < len(m) and m[j] == m[j+3] and m[j] == m[j+4]:
                qs.add(m[j])

    return ts, qs


keys = []

i = 0
pi = 0
while len(keys) < 64:
    while pi < i + 1002:
        ts, qs = process(pi)
        if ts:
            trips[pi] = ts
        if qs:
            for q in qs:
                quints.setdefault(q,set()).add(pi)
        pi += 1

    if i in trips:
        j = trips[i]
        for k in quints.get(j,[]):
            if k > i:
                keys.append(i)
                print(len(keys),i,k, k-i)
                break
    i += 1

print(keys)
