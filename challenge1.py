import networkx as nx
import matplotlib.pyplot as plt

# Membuat graf
G = nx.Graph()

# Menambahkan simpul
nodes = ['A', 'B', 'C', 'D']
G.add_nodes_from(nodes)

# Menambahkan sisi (edges)
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('C', 'A')]
G.add_edges_from(edges)

# Menggambar graf
plt.figure(figsize=(5,5))
pos = nx.spring_layout(G)  # Layout untuk graf
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, edge_color='gray', font_size=16)
plt.title("Graf dari Challenge 1")
plt.show()
