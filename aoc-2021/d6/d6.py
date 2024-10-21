#data = [3,4,3,1,2]
data = [int(x) for x in open('data').readlines()[0].strip().split(',')]

fs = {}

for f in data:
    fs[f] = fs.get(f,0) + 1

for j in range(256):
    nf = 0
    for i in range(9):
        if i not in fs:
            continue
        elif i == 0:
            nf = fs.pop(i)
        else:
            fs[i-1] = fs.pop(i)
    fs[6] = fs.get(6,0) + nf
    fs[8] = fs.get(8,0) + nf

print(sum(fs.values()))
