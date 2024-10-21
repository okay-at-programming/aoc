l = [811589153*int(x) for x in open('data')]

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
        zero = j-1

nodes[0][1].prev = nodes[-1][1]
nodes[-1][1].next = nodes[0][1]


for _ in range(10):
    for e,n in nodes:
        s = e%(len(nodes)-1)
        if s == 0:
            continue

        i = n
        for _ in range(abs(s)):
            i = i.next

        n.prev.next,n.next.prev = n.next, n.prev
        n.prev,n.next = i,i.next
        i.next.prev = n
        i.next = n


s = 0
n = nodes[zero][1]
for _ in range(3):
    for _ in range(1000):
        n = n.next
    s += n.value

print(s)
