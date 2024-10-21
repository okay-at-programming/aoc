rules = {l.split(' => ')[0].strip() : l.split(' => ')[1].strip() for l in open('data') }

def rots(rule):
    rule = rule.split('/')

    rs = []

    for _ in range(2):
        for _ in range(4):
            nr = []

            for i in range(len(rule)-1, -1, -1):
                nl = ''
                for j in range(len(rule)):
                    nl += rule[j][i]
                nr.append(nl)
            rs.append('/'.join(nr))
            rule = nr

        nr = []
        for i in range(len(rule)):
            nl = ''
            for j in range(len(rule)-1, -1, -1):
                nl += rule[i][j]
            nr.append(nl)
        rule = nr

    return rs

def div(grid, d):
    ds = []

    for y in range(0,len(grid),d):
        nl = []
        for x in range(0,len(grid),d):

            ng = []

            for i in range(y,y+d):
                s = ''
                for j in range(x,x+d):
                    s += grid[i][j]
                ng.append(s)
            nl.append('/'.join(ng))
        ds.append(nl)

    return ds

nrs = {}

for k,v in rules.items():
    for r in rots(k):
        nrs[r] = v

rules = nrs


grid = '.#./..#/###'

for _ in range(18):
    ga = grid.split('/')

    d = None
    if len(ga)%2 == 0:
        d = 2
    elif len(ga)%3 == 0:
        d = 3

    nga = []

    for l in div(ga,d):
        nl = [rules[c].split('/') for c in l]
        for i in range(len(nl[0])):
            s = ''
            for c in nl:
                s += c[i]
            nga.append(s)

    grid = '/'.join(nga)

c = 0
for l in grid.split('/'):
    c += l.count('#')
    print(l)

print(c)
