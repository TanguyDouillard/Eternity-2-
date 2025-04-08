from noeud import Noeud
from listeNoeud import ListeNoeud
import threading
import time
import random
# from ecran import *
from variables import *
import pygame

def explorer_profondeur(noeud_initial, grille_jeu, pieces, screen):
    from game import draw_ecran
    stack = [noeud_initial]
    visited = set()
    
    while stack:
        noeud = stack.pop()
        
        # Mise à jour VISIBLE immédiate
        grille_jeu.clear()
        grille_jeu.update(noeud.grille)
        pieces_restantes = noeud.pieces_a_placer
        
        # Dessin direct (sans passer par des événements)
        # screen.fill((255, 255, 255))
        
        # Dessin de la grille
        for (lig, col), piece in noeud.grille.items():
            piece.rect.x = 50 + col * piece.taille_piece
            piece.rect.y = 200 + lig * piece.taille_piece
            piece.draw(screen)
        for piece in pieces_restantes:
            piece.draw(screen)
        
        pygame.display.flip()
        # pygame.time.delay(300)  # Délai visible
        draw_ecran()
        
        if noeud.est_solution():
            return noeud
            
        enfants = noeud.generer_enfants()
        stack.extend(enfants)
    
    return None
