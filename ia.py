import matplotlib.pyplot as plt
import networkx as nx

def afficher_arbre():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5)])

    plt.figure(figsize=(5, 5))
    nx.draw(G, with_labels=True, node_color="skyblue", edge_color="gray")
    plt.show()
