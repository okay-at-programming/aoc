state = {}
x,y = 0,0
size = 50

for line in open('data'):
    x = 0
    for c in line:
        if c != '.':
            state[(x,y)] = c
        x += 1
    y += 1

for _ in range(10):
    newstate = {}
    for y in range(size):
        for x in range(size):
            tc, lc = 0, 0

            for d in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]:
                if state.get(d, '') == '|':
                    tc += 1
                elif state.get(d, '')  == '#':
                    lc += 1

            if (x,y) not in state:
                if tc >= 3:
                    newstate[(x,y)] = '|'
            elif state.get((x,y), '') == '|':
                if lc >= 3:
                    newstate[(x,y)] = '#'
                else:
                    newstate[(x,y)] = '|'
            elif state.get((x,y), '') == '#' and tc >= 1 and lc >= 1:
                newstate[(x,y)] = '#'

    state = newstate


lc,tc = 0,0
y = 0
for y in range(size):
    l = ''
    for x in range(size):
        if (x,y) in state:
            if state[(x,y)] == '|':
                tc += 1
            else:
                lc += 1
            l += state[(x,y)]
        else:
            l += '.'
    print(l)

print()
print(tc,lc,tc*lc)

