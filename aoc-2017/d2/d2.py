sheet = [[int(x) for x in y.split()] for y in open('data')]

checksum = 0
for l in sheet:
    checksum += max(l) - min(l)

print(checksum)
