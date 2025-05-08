from noeud import Noeud
from listeNoeud import ListeNoeud
import threading
import time
import random
# from ecran import *
from variables import *
import pygame

lock = threading.Lock()

if not pygame.get_init():
    pygame.init()

# def explorer_profondeur(noeud_initial, grille_jeu, pieces, screen):
#     from game import draw_ecran
#     stack = [noeud_initial]
    
    
#     while stack:
        
#         if not pygame.display.get_init():
#             return None
        
#         noeud = stack.pop()
                
#         # Mise à jour VISIBLE immédiate
#         grille_jeu.clear()
#         grille_jeu.update(noeud.grille)
#         pieces_restantes = noeud.pieces_a_placer
        
#         # Dessin direct (sans passer par des événements)
#         # screen.fill((255, 255, 255))
        
#         # Dessin de la grille
#         for (lig, col), piece in noeud.grille.items():
#             piece.rect.x = 50 + col * piece.taille_piece
#             piece.rect.y = 200 + lig * piece.taille_piece
#             piece.draw(screen)
#         for piece in pieces_restantes:
#             piece.draw(screen)
            
#         if pygame.display.get_init():
#             try:
#                 pygame.display.flip()
#                 draw_ecran()  
#                 #pygame.time.delay(150)  # Délai visible
#             except pygame.error:
#                 return None
#         # pygame.time.delay(300)  # Délai visible

#         if noeud.est_solution():
#             return noeud
            
#         enfants = noeud.generer_enfants()
#         stack.extend(enfants)
    
    # return None

def explorer_profondeur(noeud_initial, grille_jeu, pieces, screen):
    from game import ia_state, x_debut, y_debut, taille_piece, draw_ecran
    global grille_en_cours, pieces_restantes
    
    stack = [noeud_initial]
    
    while stack and not ia_state["stop_requested"]:
        if not pygame.display.get_init():
            return None
            
        noeud = stack.pop()
        
        # Met à jour l'affichage sans modifier la grille réelle
        for (lig, col), piece in noeud.grille.items():
            piece.rect.x = x_debut + col * taille_piece
            piece.rect.y = y_debut + lig * taille_piece
            piece.draw(screen)
            
            
        for piece in noeud.pieces:
            piece.draw(screen)
        
        
        pygame.display.flip()
        draw_ecran()
        pygame.time.delay(50)

        with lock:
            grille_en_cours = noeud.grille
            pieces_restantes = noeud.pieces
        
        if noeud.est_solution():
            return noeud
            
        enfants = noeud.generer_enfants()
        stack.extend(enfants)
    
    return None