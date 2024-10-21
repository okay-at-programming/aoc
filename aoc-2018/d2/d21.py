twocount = 0
threecount = 0

for line in open('test', 'r'):
    d = {}
    for char in line:
        if char not in d:
            d[char] = 0

        d[char] += 1

    counttwo = True
    countthree = True

    for key, value in d.items():
        if counttwo and value == 2:
            twocount += 1
            counttwo = False
        elif countthree and value == 3:
            threecount += 1
            countthree = False

print(twocount*threecount)
