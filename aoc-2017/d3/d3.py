test = [1,12,23,1024]
data = [289326]

for t in data:
    i = 1
    sl = 2
    while i + 4*sl < t:
        i += 4*sl
        sl += 2
    mins = sl//2
    maxs = 2*mins
    md = maxs-1
    d = -1
    while i < t:
        i += 1
        md += d
        if md == mins:
            d = 1
        if md == maxs:
            d = -1
    print(t, md-1)
