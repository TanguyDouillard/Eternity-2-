# import pygame
# from variables import *
# from utils import *

# def draw_ecran(couleur_fond_ecran, couleur_fond_grille, couleur_grille, couleur_grille_lignes, couleur_titre, couleur_titre_regles, couleur_texte_regles, couleur_fond_regles, couleur_contour_regles, choix_grille, largeur_screen, logo, x_debut_regles, son_jouable, image_son_off, image_son_on, y_debut_regles, regles, taille_piece, couleur_bouton_2, couleur_hover_bouton_2, couleur_texte_bouton_2, pieces):
#     global bouton_retour, bouton_quitter, bouton_ia, bouton_son, bouton_regles   
#     from variables import screen
    
#     pygame.init()
    
#     try:
#         font_titre = pygame.font.Font("Orbitron/Orbitron-Regular.ttf", 25)
#         font_bouton = pygame.font.Font("Orbitron/Orbitron-Regular.ttf", 35)
#     except:
#         font_titre = pygame.font.Font(None, 50)
#         font_bouton = pygame.font.Font(None, 50)

#     x_debut, y_debut = 50, 200
    
#     screen.fill(couleur_fond_ecran)  # Effacer l'écran

#     # Dessiner la grille
#     pygame.draw.rect(screen, couleur_fond_grille, (35, 185, 510, 510))  # Fond de la grille en gris

#     for j in range(choix_grille**2):
#         i = j
#         if j % choix_grille == 0 and j != 0:
#             y_debut += taille_piece
#         if j >= choix_grille:
#             i = i % choix_grille

#         pygame.draw.rect(screen, couleur_grille, ((x_debut + (i * taille_piece)), y_debut, taille_piece, taille_piece))
#         pygame.draw.rect(screen, couleur_grille_lignes, ((x_debut + (i * taille_piece)), y_debut, taille_piece, taille_piece), width=1)

#     # Titre "Eternity II"
#     try:
#         font_titre = pygame.font.Font("Orbitron/Orbitron-Regular.ttf", 100)
#     except:
#         font_titre = pygame.font.Font(None, 100)

#     texte_titre = font_titre.render("Eternity II", True, couleur_titre)
#     screen.blit(texte_titre, (largeur_screen // 2 - texte_titre.get_width() // 2, 70 - texte_titre.get_height() // 2))

#     # Affichage du logo
#     screen.blit(logo, (10, 10))



#     ## BOUTONS

#     #Bouton retour
#     # bouton_retour = pygame.Rect(x_debut_regles - 15, 15, 200, 60)

#     # Détection du survol et sélection
#     if bouton_retour.collidepoint(pygame.mouse.get_pos()):
#         couleur_retour = couleur_hover_bouton_2
#     else:
#         couleur_retour = couleur_bouton_2

#     pygame.draw.rect(screen, couleur_retour, bouton_retour, border_radius=10)
#     texte_retour = font_bouton.render("Retour", True, couleur_texte_bouton_2)
#     screen.blit(texte_retour, (bouton_retour.x + (bouton_retour.width - texte_retour.get_width()) // 2, bouton_retour.y + (bouton_retour.height - texte_retour.get_height()) // 2))


#     #Bouton quitter
#     # bouton_quitter = pygame.Rect(x_debut_regles + (210 - 15) , 15, 200, 60)

#     # Détection du survol et sélection
#     if bouton_quitter.collidepoint(pygame.mouse.get_pos()):
#         couleur_quitter = couleur_hover_bouton_2
#     else:
#         couleur_quitter = couleur_bouton_2

#     pygame.draw.rect(screen, couleur_quitter, bouton_quitter, border_radius=10)
#     texte_quitter = font_bouton.render("Quitter", True, couleur_texte_bouton_2)
#     screen.blit(texte_quitter, (bouton_quitter.x + (bouton_quitter.width - texte_quitter.get_width()) // 2, bouton_quitter.y + (bouton_quitter.height - texte_quitter.get_height()) // 2))

#     ##TEST POUR IA
#     #Bouton ia
#     # bouton_ia = pygame.Rect(x_debut_regles + 210 - 15, 80, 95, 50)

#     # Détection du survol et sélection
#     if bouton_ia.collidepoint(pygame.mouse.get_pos()):
#         couleur_ia = couleur_hover_bouton_2
#     else:
#         couleur_ia = couleur_bouton_2

#     pygame.draw.rect(screen, couleur_ia, bouton_ia, border_radius=10)
#     texte_ia = font_bouton.render("IA", True, couleur_texte_bouton_2)
#     screen.blit(texte_ia, (bouton_ia.x + (bouton_ia.width - texte_ia.get_width()) // 2, bouton_ia.y + (bouton_ia.height - texte_ia.get_height()) // 2))
#     ##FIN TEST IA


#     #Bouton son
#     # bouton_son = pygame.Rect(x_debut_regles + (210 - 15)  + 100, 80, 100, 50)

#     # Détection du survol et sélection
#     if bouton_son.collidepoint(pygame.mouse.get_pos()):
#         couleur_son = couleur_hover_bouton_2
#     else:
#         couleur_son = couleur_bouton_2

#     pygame.draw.rect(screen, couleur_son, bouton_son, border_radius=10)
#     if son_jouable == True:
#         screen.blit( image_son_on, ( x_debut_regles + (210 - 15)  + 100 + 30, 85) )
#     else:
#         screen.blit( image_son_off, ( (x_debut_regles + (210 - 15)  + 100) + 30 , 85) )
        
        
#     #Bouton Règles    
#     # bouton_regles = pygame.Rect(x_debut_regles - 15, 80, 200, 50)
    
#     # Détection du survol et sélection
#     if bouton_regles.collidepoint(pygame.mouse.get_pos()):
#         couleur_regles = couleur_hover_bouton_2
#     else:
#         couleur_regles = couleur_bouton_2
        
#     pygame.draw.rect(screen, couleur_regles, bouton_regles, border_radius=10)
#     texte_regles = font_bouton.render("regles", True, couleur_texte_bouton_2)
#     screen.blit(texte_regles, (bouton_regles.x + (bouton_regles.width - texte_regles.get_width()) // 2, bouton_regles.y + (bouton_regles.height - texte_regles.get_height()) // 2))
    
    
#     affichage_regles(regles,couleur_titre_regles,x_debut_regles,y_debut_regles, screen, couleur_fond_regles, couleur_contour_regles, couleur_texte_regles, couleur_fond_ecran)
