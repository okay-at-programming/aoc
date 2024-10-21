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
    if r:
        return r
    r = True

    for i in range(len(b)):
        if not b[i][y][1]:
            r = False

    return r

def win(b,c):
    s = 0
    for l in b:
        for m in l:
            if not m[1]:
                s += m[0]
    print(s,c,s*c)

bc = len(boards)

for c in calls:
    nb = []
    for b in boards:
        w = False
        for x in range(len(b)):
            for y in range(len(b[x])):
                if b[x][y][0] == c:
                    b[x][y] = c,True
                    if check(b,x,y):
                        w = True
                        if len(boards) == 1:
                            win(b,c)
                    break
                else:
                    continue
                break
            else:
                continue
            break

        if not w:
            nb.append(b)
    boards = nb
