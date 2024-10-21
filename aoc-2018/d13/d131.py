grid = []

class cart:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.t = 0

    def getkey(self):
        return self.y, self.x

    def getpos(self):
        return self.x, self.y

    def next(self):
        nx = self.x
        ny = self.y
        if self.shape == '^':
            ny -= 1
            if grid[ny][nx] == '\\':
                self.shape = '<'
            elif grid[ny][nx] == '/':
                self.shape = '>'
            elif grid[ny][nx] == '+':
                d = self.t % 3
                if d == 0:
                    self.shape = '<'
                elif d == 2:
                    self.shape = '>'
                self.t += 1
        elif self.shape == '>':
            nx += 1
            if grid[ny][nx] == '\\':
                self.shape = 'v'
            elif grid[ny][nx] == '/':
                self.shape = '^'
            elif grid[ny][nx] == '+':
                d = self.t % 3
                if d == 0:
                    self.shape = '^'
                elif d == 2:
                    self.shape = 'v'
                self.t += 1
        elif self.shape == 'v':
            ny += 1
            if grid[ny][nx] == '\\':
                self.shape = '>'
            elif grid[ny][nx] == '/':
                self.shape = '<'
            elif grid[ny][nx] == '+':
                d = self.t % 3
                if d == 0:
                    self.shape = '>'
                elif d == 2:
                    self.shape = '<'
                self.t += 1
        elif self.shape == '<':
            nx -= 1
            if grid[ny][nx] == '\\':
                self.shape = '^'
            elif grid[ny][nx] == '/':
                self.shape = 'v'
            elif grid[ny][nx] == '+':
                d = self.t % 3
                if d == 0:
                    self.shape = 'v'
                elif d == 2:
                    self.shape = '^'
                self.t += 1
        self.x = nx
        self.y = ny
        return nx,ny

carts = []

y = 0
for line in open('data', 'r'):
    line = line[:-1]
    row = []
    x = 0

    for c in line:
        if c in ['^', 'v', '>', '<']:
            car = cart(x, y, c)
            carts.append(car)

            if c in ['^', 'v']:
                row.append('|')
            else:
                row.append('-')
        else:
            row.append(c)

        x += 1

    grid.append(row)
    y += 1

def key(c):
    return c.getkey()

cont = True
i = 0
while cont:
    newpos = set()
    oldpos = set()

    for cart in carts:
        oldpos.add(cart.getpos())

    for cart in carts:
        old = cart.getpos()
        new = cart.next()

        if new in oldpos:
            cont = False
            print(new)

        if new in newpos:
            cont = False
            print(new)

        oldpos.remove(old)

        newpos.add(new)
    carts.sort(key=key)
