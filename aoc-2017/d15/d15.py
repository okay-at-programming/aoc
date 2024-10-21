
amul = 16807
bmul = 48271
div = 2147483647

aprev = 277
bprev = 349
c = 0
for _ in range(40000000):
    a = (amul*aprev)%div
    b = (bmul*bprev)%div
    ea = a%65536
    eb = b%65536
    if ea == eb:
        c += 1
    aprev,bprev = a, b

print(c)
