tx = 20,30
ty = -10,-5
#target area: x=281..311, y=-74..-54
tx = 281,311
ty = -74,-54

def throw(vx,vy,tx,ty):
    x,y = 0,0

    while x <= tx[1] and y >= ty[0]:
        x += vx
        y += vy

        if x >= tx[0] and x <= tx[1] and y >= ty[0] and y <= ty[1]:
            return 1

        if vx > 0:
            vx -= 1
        vy -= 1


c = 0
for vx in range(1000):
    for vy in range(ty[0],1000):
        y = throw(vx,vy,tx,ty)
        if y:
            c += 1

print(c)
