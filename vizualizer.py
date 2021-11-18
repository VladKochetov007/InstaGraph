import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([("2","3")], weight=1)
#KG = nx.complete_graph(G)


pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size = 500)
nx.draw_networkx_labels(G, pos)
plt.show()