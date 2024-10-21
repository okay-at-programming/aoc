tx = 20,30
ty = -10,-5
#target area: x=281..311, y=-74..-54
tx = 281,311
ty = -74,-54

def throw(vx,vy,tx,ty):
    x,y,my = 0,0,None

    while x <= tx[1] and y >= ty[0]:
        x += vx
        y += vy

        if x >= tx[0] and x <= tx[1] and y >= ty[0] and y <= ty[1]:
            return my

        if vx > 0:
            vx -= 1
        vy -= 1
        if vy == 0:
            my = y

print(7,2,throw(7,2,tx,ty))
print(6,3,throw(6,3,tx,ty))
print(9,0,throw(9,0,tx,ty))
print(17,-4,throw(17,-4,tx,ty))

my = 0
for vx in range(1000):
    for vy in range(1000):
        y = throw(vx,vy,tx,ty)
        if y and y > my:
            my = y

print(my)
