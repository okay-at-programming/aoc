a,b,c,d,e,f = 0,0,0,0,0,0

seen = set()

c = 65536
d = 1397714
while True:
    d = (65899 * ((d + (c & 255)) & 16777215)) & 16777215

    if 256 > c:
        if d in seen:
            break
        print(c, d)
        seen.add(d)
        c = d | 65536
        d = 1397714
        continue

    c = c//256
