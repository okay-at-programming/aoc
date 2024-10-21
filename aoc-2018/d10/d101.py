def parse(line):
    a, b = line.split(', ')
    return int(a), int(b)

class point:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def __str__(self):
        return str(self.x) + ', ' + str(self.y) + ' - ' + str(self.dx) + ', ' + str(self.dy)

points = []

for line in open('test', 'r'):
    chev = line.find('<') + 1
    chev2 = line.find('>')
    y, x = parse(line[chev:chev2])
    chev = line.find('<', chev) + 1
    chev2 = line.find('>', chev)
    dy, dx = parse(line[chev:chev2])

    p = point(x, y, dx, dy)
    points.append(p)

def getrange(points):
    minx = None
    miny = None
    maxx = None
    maxy = None

    for p in points:
        if miny == None or p.y < miny:
            miny = p.y
        if maxy == None or p.y > maxy:
            maxy = p.y

        if minx == None or p.x < minx:
            minx = p.x
        if maxx == None or p.x > maxx:
            maxx = p.x

    return minx, miny, maxx, maxy

minx, miny, maxx, maxy = getrange(points)

rangex = maxx-minx+1
rangey = maxy-miny+1

for it in range(20000):
    if rangex < 100 and rangey < 100:
        grid = [[None]*rangey for i in range(rangex)]

        for p in points:
            grid[p.x-minx][p.y-miny] = 'X'

        print('')
        print('- - - - - - - - -')
        print('')
        print(it)
        print('')

        for row in grid:
            line = ''
            for cell in row:
                line += '.' if cell == None else 'X'
            print(line)

    for p in points:
        p.x = p.x + p.dx
        p.y = p.y + p.dy

    minx, miny, maxx, maxy = getrange(points)
    rangex = maxx - minx + 1
    rangey = maxy - miny + 1
