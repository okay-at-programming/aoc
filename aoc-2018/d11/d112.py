def power(x, y, sn):
    rid = x+10
    i = rid * y
    i += sn
    i *= rid
    i = int(i/100)%10
    return i-5

sn = 2187
maxx = 300

grid = [[None]*maxx for i in range(maxx)]

for i in range(maxx):
    for j in range(maxx):
        grid[i][j] = power(i+1,j+1,sn)

maxpower = 0
maxpowercoord = None

for size in range(maxx, 0, -1):
    print(size)
    for i in range(300 - size + 1):
        for j in range(300 - size + 1):
            power = sum(sum(r[j:j+size]) for r in grid[i:i+size])
            if power > maxpower:
                maxpower = power
                maxpowercoord = i+1,j+1,size
                print(maxpowercoord)

print(maxpower)
print(maxpowercoord)

