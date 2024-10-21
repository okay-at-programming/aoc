import networkx as nx

g = nx.Graph()

for l in open('data'):
    n,r = l.strip().split(':')

    for o in r.strip().split():
        g.add_edge(n,o)

print(g)

c,p = nx.stoer_wagner(g)
print(c)
print(len(p[0])*len(p[1]))
