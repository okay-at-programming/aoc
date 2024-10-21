
class monkey:
    def __init__(self, items, op, test, tr, fa):
        self.items = items
        self.op = op
        self.test = test
        self.tr = tr
        self.fa = fa
        self.insc = 0

    def turn(self):
        if len(self.items) == 0:
            return None
        self.insc += 1
        item = self.items.pop(0)
        item = self.oper(item)
        item = item // 3
        if item % self.test == 0:
            return self.tr, item
        return self.fa, item


    def oper(self, item):
        a,b,c = self.op.split()
        if a == 'old':
            a = item
        elif a.isnumeric():
            a = int(a)
        if c == 'old':
            c = item
        elif c.isnumeric():
            c = int(c)
        if b == '*':
            return a * c
        elif b == '+':
            return a + c
        assert False

d = open('data').read().strip().split('\n\n')
monks = []
for m in d:
    dl = m.split('\n')
    items = [int(x.strip()) for x in dl[1].split(':')[1].split(',')]
    op = dl[2].split('=')[1].strip()
    test = int(dl[3].strip().split()[-1])
    tr = int(dl[4].strip().split()[-1])
    fa = int(dl[5].strip().split()[-1])
    monk = monkey(items,op,test,tr,fa)
    monks.append(monk)

for _ in range(20):
    for m in monks:
        while True:
            r = m.turn()
            if not r:
                break
            monks[r[0]].items.append(r[1])

r = sorted([m.insc for m in monks])
print(r[-1]*r[-2])

