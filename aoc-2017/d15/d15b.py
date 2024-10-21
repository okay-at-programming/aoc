
amul = 16807
bmul = 48271
div = 2147483647

aprev = 277
bprev = 349
c = 0
for _ in range(5000000):
    a = (amul*aprev)%div
    while a%4 != 0:
        a = (amul*a)%div
    b = (bmul*bprev)%div
    while b%8 != 0:
        b = (bmul*b)%div
    ea = a%65536
    eb = b%65536
    if ea == eb:
        c += 1
    aprev,bprev = a, b

print(c)
