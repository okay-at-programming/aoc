sheet = [[int(x) for x in y.split()] for y in open('data')]

checksum = 0
for l in sheet:
    for a in l:
        for b in l:
            if b <= a:
                continue
            if b%a == 0:
                print(b,a)
                checksum += b//a

print(checksum)
