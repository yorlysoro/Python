import networkx as nx

g = nx.Graph()
g.add_edge('a', 'b', weight=0.1)
g.add_edge('b', 'c', weight=1.5)
g.add_edge('a', 'c', weight=1.0)
g.add_edge('c', 'd', weight=2.2)
print(nx.shortest_path(g, 'b', 'd'))
print(nx.shortest_path(g, 'a', 'd', weight=True))

