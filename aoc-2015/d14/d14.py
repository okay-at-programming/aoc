total_time = 2503

m = 0

for l in open('data'):
    r = l.split()[0]
    pace, time, rest = [int(i) for i in l.split() if i.isdigit()]

    d = (total_time // (time + rest) ) * pace * time
    d += min(total_time % (time + rest), time) * pace

    if d > m:
        m = d

    print(r, d)

print(m)
