calls = None
boards = []
board = []

for l in open('data'):
    if not calls:
        calls = [int(x) for x in l.strip().split(',')]
    elif len(l) > 1:
        board.append([(int(x),False) for x in l.strip().split(' ') if x])
    elif len(board) > 1:
        boards.append(board)
        board = []
boards.append(board)

def check(b,x,y):
    r = True
    for c in b[x]:
        if not c[1]:
            r = False

    for i in range(len(b)):
        if not b[i][y]:
            r = False

    return r

def win(b,c):
    s = 0
    for l in b:
        for m in l:
            if not m[1]:
                s += m[0]
    print(s,c,s*c)
done = False
for c in calls:
    for b in boards:
        for x in range(len(b)):
            for y in range(len(b[x])):
                if b[x][y][0] == c:
                    b[x][y] = c,True
                    if check(b,x,y):
                        win(b,c)
                        done = True
                    break
                else:
                    continue
                break
            else:
                continue
            break
        if done:
            break
    if done:
        break




