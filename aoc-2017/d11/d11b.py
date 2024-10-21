test = ['ne,ne,ne','ne,ne,sw,sw','ne,ne,s,s','se,sw,se,sw,sw']
data = [open('data').read().strip()]
#data = test

moves = {'n':(0,2),'ne':(1,1),'se':(1,-1),'s':(0,-2),'sw':(-1,-1),'nw':(-1,1)}

for d in data:
    pos = 0,0
    b = 0

    for step in d.split(','):
        move = moves[step]
        pos = pos[0]+move[0],pos[1]+move[1]

        t = (abs(pos[0])+abs(pos[1]))//2

        if t > b:
            b = t
    print(b)
