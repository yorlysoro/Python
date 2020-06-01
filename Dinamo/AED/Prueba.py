import networkx as nx
import matplotlib.pyplot as plt
 
n = 7
G1 = nx.complete_graph(n-1)
G2 = nx.complete_graph(n)
G3 = nx.complete_graph(n-1)
nx.draw_circular(G1, ax=plt.axes((.3, .01+.25*2, .3, .22)))
nx.draw_circular(G2, ax=plt.axes((.3, .01+.25, .3, .22)))
nx.draw_circular(G3, ax=plt.axes((.3, .01, .3, .22)))
plt.show()
