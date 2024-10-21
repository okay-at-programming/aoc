def pa(op, j):
    a = op.split()[j]
    if a == 'old':
        return lambda i: i
    return lambda i: int(a)

def po(op):
    b = op.split()[1]
    if b == '*':
        return lambda a,b: a*b
    return lambda a,b: a+b


class monkey:
    def __init__(self, items, op, test, tr, fa):
        self.items = items
        self.a = pa(op, 0)
        self.b = pa(op,2)
        self.op = po(op)
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
        if item % self.test == 0:
            return self.tr, item
        return self.fa, item


    def oper(self, item):
        a = self.a(item)
        b = self.b(item)
        return self.op(a,b)

d = open('data').read().strip().split('\n\n')
monks = []
p = 1
for m in d:
    dl = m.split('\n')
    items = [int(x.strip()) for x in dl[1].split(':')[1].split(',')]
    op = dl[2].split('=')[1].strip()
    test = int(dl[3].strip().split()[-1])
    tr = int(dl[4].strip().split()[-1])
    fa = int(dl[5].strip().split()[-1])
    monk = monkey(items,op,test,tr,fa)
    monks.append(monk)
    p *= test


for i in range(10000):
    for m in monks:
        while True:
            r = m.turn()
            if not r:
                break
            monks[r[0]].items.append(r[1]%p)
    if i%1000 == 0:
        print(i,[m.insc for m in monks])

print(i,[m.insc for m in monks])

r = sorted([m.insc for m in monks])
print(r[-1]*r[-2])

