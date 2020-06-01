import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

G.add_node("Berea")
G.add_nodes_from(range(1,10))

G.remove_node("Berea")
G.remove_nodes_from([(1,2), (2,3)])

G.add_edge(5, 100)
G.remove_edge(5,100)

G.add_weighted_edges_from([(0,1,3,0), (3,4,7.5)])
G.add_path([1,2,3])

nx.draw(G, with_labels = True)
plt.draw()
plt.show()
