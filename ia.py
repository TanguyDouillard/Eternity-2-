import matplotlib.pyplot as plt
import networkx as nx
import time 
import pygame
from ecran import *

def afficher_arbre():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5)])

    plt.figure(figsize=(5, 5))
    nx.draw(G, with_labels=True, node_color="skyblue", edge_color="gray")
    plt.show()

# def run_ia():
#     global grille_jeu, pieces, ia_running

#     # Logique de l'IA ici
#     while ia_running:
#         # Exemple de logique d'IA
#         # Vous pouvez utiliser votre méthode d'exploration en profondeur ici
#         print("IA is running...")
#         time.sleep(1)  # Simuler le travail de l'IA

#         # Mettre à jour l'affichage ou les pièces selon les actions de l'IA
#         draw_ecran(screen)
#         for piece in pieces:
#             piece.draw(screen)
#         pygame.display.flip()

#         # Condition d'arrêt de l'IA
#         if len(grille_jeu) == choix_grille**2:
#             ia_running = False