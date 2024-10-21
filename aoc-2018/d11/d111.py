def power(x, y, sn):
    rid = x+10
    i = rid * y
    i += sn
    i *= rid
    i = int(i/100)%10
    return i-5

sn = 18
maxx = 300

grid = [[None]*300 for i in range(300)]

for i in range(300):
    for j in range(300):
        grid[i][j] = power(i+1,j+1,sn)

maxpower = 0
maxpowercoord = None
for i in range(maxx):
    for j in range(maxx):
        for size in range(maxx - max(i, j)):
            power = 0
            for k in range(size):
                for l in range(size):
                    power += grid[i+k][j+l]
            if power > maxpower:
                maxpower = power
                maxpowercoord = i+1,j+1,size

print(maxpower)
print(maxpowercoord)

