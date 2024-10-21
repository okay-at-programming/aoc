l = [int(x) for x in open('data')]

class Node:
    def __init__(self,value, i):
        self.value = value
        self.i = i

zero = 0
nodes = []
j = 0
for i in l:
    node = Node(i,j)
    if j > 0:
        node.prev = nodes[-1][1]
        nodes[-1][1].next = node
    nodes.append((i,node))
    j += 1
    if i == 0:
        print('zero')
        zero = j-1

nodes[0][1].prev = nodes[-1][1]
nodes[-1][1].next = nodes[0][1]


for e,n in nodes:
    if e == 0:
        continue

    i = n
    for _ in range(abs(e)):
        if e > 0:
            i = i.next
            if i.i == n.i:
                i = i.next
        else:
            i = i.prev
            if i.i == n.i:
                i = i.prev

    if e < 0:
        i = i.prev
        if i.i == n.i:
            i = i.prev

    n.prev.next,n.next.prev = n.next, n.prev
    n.prev,n.next = i,i.next
    i.next.prev = n
    i.next = n


s = 0
n = nodes[zero][1]
print(zero, n.value, len(nodes))
for _ in range(3):
    for _ in range(1000):
        n = n.next
    s += n.value
    print(n.value,s)

print(s)
assert False

n = nodes[0][1]
for _ in range(len(nodes)):
    print(n.value)
    n = n.next



