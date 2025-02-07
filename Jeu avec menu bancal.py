#Importation des bibliothèques
import pygame
import random
import time

# Initialisation de Pygame
pygame.init()


#Importation images
logo = pygame.image.load("Images\Polytech_logo.png")
logo = pygame.transform.scale(logo, (373, 125))

# Dimensions de la fenêtre
largeur_screen,longueur_screen = 1500 , 750
screen = pygame.display.set_mode((largeur_screen, longueur_screen))
pygame.display.set_caption("Eternity ii")


#Choix de la taille de la grille + taille de la pièce + coordonnées en haut à gauche de la grille
choix_grille = random.choice([4,6,8,12,16]) #A modifier en fonction du choix de l'utilisateur !
taille_piece = 480//choix_grille
x_debut , y_debut = 50,200

x_debut_regles , y_debut_regles = 1100 , 185



#####################################################

#################################################

## Choix style de jeu (couleur)

liste_palette = ["Classique" , "Néon" , "Pastel"]
palette_couleur = random.choice(liste_palette)

def modification_style(palette_couleur):

    global couleur_fond_ecran ,couleur_fond_grille, couleur_grille, couleur_grille_lignes, couleur_titre, couleur_titre_regles, couleur_texte_regles, couleur_fond_regles, couleur_contour_regles


    if palette_couleur == "Classique" :

        couleur_fond_ecran = "lightblue"
        couleur_fond_grille = (127, 140, 141) #Gris
        couleur_grille = "black"
        couleur_grille_lignes = "white"
        couleur_titre = "black"
        couleur_titre_regles = "black"
        couleur_texte_regles = "black"
        couleur_fond_regles = (220, 220, 220)  # Gris clair
        couleur_contour_regles = (100, 100, 100)


    elif palette_couleur == "Pastel" :

        couleur_fond_ecran = (245, 245, 220) #Beige Pastel
        couleur_fond_grille = (173, 216, 230) #Bleu Pastel
        couleur_grille = "grey50"
        couleur_grille_lignes = (189, 252, 201) #Menthe Pastel
        couleur_titre = (255, 182, 193) #Corail Pastel
        couleur_titre_regles = (255, 182, 193) #Corail Pastel
        couleur_texte_regles = "grey50"
        couleur_fond_regles = (173, 216, 230) #Bleu Pastel
        couleur_contour_regles = (189, 252, 201) #Menthe Pastel


    elif palette_couleur == "Néon" :

        couleur_fond_ecran = "grey5"
        couleur_fond_grille = (0, 229, 229) #Turquoise Néon
        couleur_grille = "grey20"
        couleur_grille_lignes = (255, 0, 127) #Rose Néon
        couleur_titre = (255, 0, 127) #Rose Néon
        couleur_titre_regles = (255, 0, 127) #Rose Néon
        couleur_texte_regles = (255, 94, 0) #Orange Néon
        couleur_fond_regles = (0, 229, 229) #Turquoise Néon
        couleur_contour_regles = (255, 0, 127) #Rose Néon




#Création de l'écran (fond, grille etc...)
def draw_ecran():
    global choix_grille, taille_piece, couleur_fond_ecran ,couleur_fond_grille, couleur_grille, couleur_grille_lignes, couleur_titre, couleur_titre_regles, couleur_texte_regles, couleur_fond_regles, couleur_contour_regles


    x_debut, y_debut = 50, 200
    screen.fill(couleur_fond_ecran)  # Effacer l'écran

    # Dessiner la grille
    pygame.draw.rect(screen, couleur_fond_grille, (35, 185, 510, 510))  # Fond de la grille en gris

    for j in range(choix_grille**2):
        i = j
        if j % choix_grille == 0 and j != 0:
            y_debut += taille_piece
        if j >= choix_grille:
            i = i % choix_grille

        pygame.draw.rect(screen, couleur_grille, ((x_debut + (i * taille_piece)), y_debut, taille_piece, taille_piece))
        pygame.draw.rect(screen, couleur_grille_lignes, ((x_debut + (i * taille_piece)), y_debut, taille_piece, taille_piece), width=1)

    # Titre "Eternity II"
    try:
        font_titre = pygame.font.Font("Orbitron/Orbitron-Regular.ttf", 100)
    except:
        font_titre = pygame.font.Font(None, 100)

    texte_titre = font_titre.render("Eternity II", True, couleur_titre)
    screen.blit(texte_titre, (largeur_screen // 2 - texte_titre.get_width() // 2, 70 - texte_titre.get_height() // 2))

    # Affichage du logo
    screen.blit(logo, (10, 10))

    # ITRE "RÈGLES"
    try:
        font_titre_regles = pygame.font.Font("Orbitron/Orbitron-Regular.ttf", 30)
    except:
        font_titre_regles = pygame.font.Font(None, 35)

    titre_regles = font_titre_regles.render("RÈGLES", True, couleur_titre_regles)  # Noir
    screen.blit(titre_regles, (x_debut_regles + 120, y_debut_regles - 50))  # Centré au-dessus du texte

    # TEXTE DES RÈGLES (bien structuré)
    texte_regles = """Bienvenue dans Eternity II !

Le but du jeu est d'assembler
toutes les pièces dans la grille
de manière à ce que les couleurs
des côtés adjacents
correspondent.

Attention !
Tu ne peux pas poser deux
pièces l'une à coté de l'autre
si elle n'ont pas les bords de
même couleur.
Les pièces en bordure doivent
coincider avec la couleur du bord.

Commandes :
- Clic gauche : déplacer une pièce
- Clic droit : faire pivoter une pièce

Bonne chance !"""

    # Définition de la zone d'affichage
    rect_zone = pygame.Rect(x_debut_regles, y_debut_regles, 375, 520)  # Hauteur ajustée
    #couleur_fond = (220, 220, 220)  # Gris clair

    # Police et taille du texte
    try:
        font_regles = pygame.font.Font("Orbitron/Orbitron-Regular.ttf", 20)
    except:
        font_regles = pygame.font.Font(None, 25)

    # Affichage du fond de la zone
    pygame.draw.rect(screen, couleur_fond_regles, rect_zone, border_radius=10)  # Bord arrondi

    # Découper et afficher le texte proprement
    lignes = texte_regles.split("\n")  # Séparer les lignes avec "\n"
    y = rect_zone.top + 10  # Décalage du haut

    for ligne in lignes:
        if ligne.strip() == "":  # Vérifier si la ligne est vide pour ajouter un espace vertical
            y += font_regles.get_height() // 2
        else:
            texte_render = font_regles.render(ligne, True, couleur_texte_regles)  # Noir
            screen.blit(texte_render, (rect_zone.left + 5, y))
            y += font_regles.get_height()

    # Afficher le contour du rectangle
    pygame.draw.rect(screen, couleur_contour_regles, rect_zone, width=2, border_radius=10)


###########################################

#Créer pièces
class Piece:

    #Initialisation
    def __init__(self, id_piece, x, y, cotes, couleurs):
        self.id_piece = id_piece
        self.x = x
        self.y = y
        self.cotes = cotes  # Haut, Droite, Bas, Gauche
        self.couleurs = couleurs
        self.rotation = 0  # Rotation actuelle (0, 90, 180, 270)
        self.rect = pygame.Rect(x, y, taille_piece, taille_piece)

        self.colonne = round((self.rect.x - x_debut) / taille_piece)
        self.ligne   = round((self.rect.y - y_debut) / taille_piece)    # Position ligne sur la grille (0 à choix_grille - 1)


    # Rotation de 90 degrés (changer l'ordre des bords)
    def rotate(self):
        self.couleurs = self.couleurs[-1:] + self.couleurs[:-1]
        self.cotes = self.cotes[-1:] + self.cotes[:-1]
        self.rotation = (self.rotation + 90) % 360


    # Dessiner la pièce avec ses triangles colorés
    def draw(self, surface):
        cx, cy = self.rect.center  # Centre du carré
        corners = [
            (self.rect.left, self.rect.top),      # Haut-gauche
            (self.rect.right, self.rect.top),     # Haut-droit
            (self.rect.right, self.rect.bottom),  # Bas-droit
            (self.rect.left, self.rect.bottom),   # Bas-gauche
        ]

        # Triangle haut
        pygame.draw.polygon(surface, self.couleurs[0], [corners[0], corners[1], (cx, cy)])
        # Triangle droit
        pygame.draw.polygon(surface, self.couleurs[1], [corners[1], corners[2], (cx, cy)])
        # Triangle bas
        pygame.draw.polygon(surface, self.couleurs[2], [corners[2], corners[3], (cx, cy)])
        # Triangle gauche
        pygame.draw.polygon(surface, self.couleurs[3], [corners[3], corners[0], (cx, cy)])



#Lecture du fichier de création de la grille
def lire_fichier(filename):
    with open(filename, 'r') as f:
        taille_grille, nombre_couleurs = map(int, f.readline().strip().split())
        grille = []
        for ligne in f:
            piece = tuple(map(int, ligne.strip().strip('()').split(',')))
            grille.append(piece)
    return taille_grille, nombre_couleurs, grille


#Assigner des couleurs fixes aux chiffres
def generer_couleurs(nombre_couleurs, palette):
    if palette == "Pastel":
        couleurs_bases = {
            0: (173, 216, 230),  # bleu pastel
            1: (255, 182, 193),  # Rose pastel
            2: (240, 230, 140),  # Jaune pastel
            3: (144, 238, 144),  # Vert pastel
            4: (255, 223, 186),  # Orange pastel
            5: (221, 160, 221),  # Violet pastel
            6: (240, 128, 128),  # Rouge pastel
            7: (255, 255, 153),  # Jaune pastel
            8: (200, 200, 200),  # gris pastel
            9: (255, 218, 185),  # Pêche pastel
            10: (152, 251, 152),  # Vert menthe pastel
            11: (255, 192, 203),  # Rose bonbon pastel
            12: (135, 206, 250),  # Bleu ciel pastel
            13: (216, 191, 216),  # Lilas pastel
            14: (255, 228, 196),  # Bisque pastel
            15: (175, 238, 238),  # Cyan pastel
            16: (255, 182, 193),  # Rose clair pastel
            17: (176, 196, 222),  # Bleu acier pastel
            18: (245, 222, 179),  # Beige pastel
            19: (255, 239, 213),  # Papaya pastel
            20: (255, 245, 238),  # Blanc coquille pastel
            21: (255, 248, 220),  # Blé pastel
            22: (230, 230, 250),  # Lavande pastel
        }
    if palette == "Classique":
        couleurs_bases = {
            0: (127, 140, 141),  # Gris
            1: (255, 87, 51),    # Rouge vif
            2: (51, 255, 87),    # Vert vif
            3: (51, 87, 255),    # Bleu vif
            4: (241, 196, 15),   # Jaune
            5: (142, 68, 173),   # Violet
            6: (26, 188, 156),   # Turquoise
            7: (231, 76, 60),    # Rouge tomate
            8: (46, 204, 113),   # Vert émeraude
            9: (52, 152, 219),   # Bleu clair
            10: (230, 126, 34),  # Orange vif
            11: (155, 89, 182),  # Mauve
            12: (52, 73, 94),    # Bleu gris
            13: (22, 160, 133),  # Vert océan
            14: (192, 57, 43),   # Rouge brique
            15: (41, 128, 185),  # Bleu profond
            16: (39, 174, 96),   # Vert forêt
            17: (243, 156, 18),  # Orange doré
            18: (211, 84, 0),    # Orange foncé
            19: (189, 195, 199), # Gris clair
            20: (149, 165, 166), # Gris bleuté
            21: (44, 62, 80),    # Bleu nuit
            22: (236, 240, 241), # Blanc cassé
        }
    if palette == "Néon":
        couleurs_bases = {
            0: (0, 229, 229),    # Turquoise Néon
            1: (255, 87, 51),    # Rouge vif
            2: (51, 255, 87),    # Vert vif
            3: (51, 87, 255),    # Bleu vif
            4: (241, 196, 15),   # Jaune
            5: (142, 68, 173),   # Violet
            6: (26, 188, 156),   # Turquoise
            7: (231, 76, 60),    # Rouge tomate
            8: (46, 204, 113),   # Vert émeraude
            9: (52, 152, 219),   # Bleu clair
            10: (255, 94, 0),  # Orange Néon
            11: (155, 89, 182),  # Mauve
            12: (52, 73, 94),    # Bleu gris
            13: (22, 160, 133),  # Vert océan
            14: (192, 57, 43),   # Rouge brique
            15: (41, 128, 185),  # Bleu profond
            16: (39, 174, 96),   # Vert forêt
            17: (243, 156, 18),  # Orange doré
            18: (255, 0, 255),    # Magenta Néon
            19: (189, 195, 199), # Gris clair
            20: (149, 165, 166), # Gris bleuté
            21: (44, 62, 80),    # Bleu nuit
            22: (236, 240, 241), # Blanc cassé
        }
    return {i: couleurs_bases.get(i) for i in range(0, nombre_couleurs)}



#Création des pièces
def creer_pieces(grille, couleurs):
    pieces = []
    for i, cotes in enumerate(grille):
        couleurs_piece = [
            couleurs[cotes[0]],  # Haut
            couleurs[cotes[1]],  # Droite
            couleurs[cotes[2]],  # Bas
            couleurs[cotes[3]],  # Gauche
        ]
        piece = Piece(i, random.randint(650, largeur_screen - (taille_piece + 50 + (largeur_screen-x_debut_regles))), random.randint(185, longueur_screen - (taille_piece + 50)), cotes, couleurs_piece)  # Par défaut, aucune position

     # Ajouter une rotation aléatoire (0, 90, 180, 270)
        rotations = random.choice([0, 1, 2, 3])  # 0 = pas de rotation, 1 = 90°, 2 = 180°, 3 = 270°
        for _ in range(rotations):
            piece.rotate()  # Appliquer la rotation

        pieces.append(piece)
    return pieces




##################################


#Création des variables nécéssaires dans la boucle run
running = True
fichier = "Grille" + str(choix_grille) + "x" + str(choix_grille) + ".txt" #A modifier en fonction de choix_grille
taille_grille, nombre_couleurs, grille = lire_fichier(fichier)

# couleurs = generer_couleurs(nombre_couleurs)
# pieces = creer_pieces(grille, couleurs)


#Création dictionnaire pour vérifier si case pleine ou pas
grille_jeu = {}  # Dictionnaire vide


#La pièce sélectionnée par l'utlisateur
selected_tile = None

##TEST MENU
scene = 1


###############################


#Boucle

while running:

    ## TEST MENU
    if scene == 1 :
        # Paramètres d'affichage
        font = pygame.font.Font(None, 50)
        couleur_fond = (200, 200, 255)
        couleur_bouton = (100, 100, 255)
        couleur_hover = (50, 50, 200)
        couleur_selection = (0, 200, 0)
        blanc = (255, 255, 255)

        tailles_possibles = [4, 6, 8, 12, 16]
        boutons = []  # Stocke les rectangles des boutons
        boutons2 = []
        choix_grille = None  # Aucune sélection au départ
        palette_couleur = None # Aucune sélection au départ

        bouton_jouer = pygame.Rect(500, 500, 200, 60)  # Bouton "Jouer"

        run = True
        while run:
            screen.fill(couleur_fond)

            # Affichage du titre
            titre = font.render("Choisissez la taille de la grille", True, (0, 0, 0))
            screen.blit(titre, (200, 100))

            # Création des boutons de sélection
            boutons.clear()
            for i, taille in enumerate(tailles_possibles):
                rect = pygame.Rect(500, 200 + i * 70, 200, 50)
                boutons.append((rect, taille))

                # Détection du survol et sélection
                if rect.collidepoint(pygame.mouse.get_pos()):
                    couleur = couleur_hover if choix_grille != taille else couleur_selection
                else:
                    couleur = couleur_selection if choix_grille == taille else couleur_bouton

                pygame.draw.rect(screen, couleur, rect, border_radius=10)

                # Affichage du texte centré dans le bouton
                texte = font.render(f"{taille}x{taille}", True, blanc)
                screen.blit(texte, (rect.x + (rect.width - texte.get_width()) // 2, rect.y + (rect.height - texte.get_height()) // 2))

            titre2 = font.render("Choisissez la couleur des pièces", True, (0, 0, 0))
            screen.blit(titre2, (800, 100))        
            
            boutons2.clear()
            for i, palette in enumerate(["Classique", "Pastel","Néon"]):
                rect = pygame.Rect(800, 200 + i * 70, 200, 50)
                boutons2.append((rect, palette))
                
                #Détection du survol et sélection
                if rect.collidepoint(pygame.mouse.get_pos()):
                    couleur = couleur_hover if palette_couleur != palette else couleur_selection
                else:
                    couleur = couleur_selection if palette_couleur == palette else couleur_bouton
                
                pygame.draw.rect(screen, couleur, rect, border_radius=10)
                
                # Affichage du texte centré dans le bouton
                texte2 = font.render(f"{palette}", True, blanc)
                screen.blit(texte2, (rect.x + (rect.width - texte2.get_width()) // 2, rect.y + (rect.height - texte2.get_height()) // 2))
                

            # Bouton "Jouer" avec effet de survol
            if bouton_jouer.collidepoint(pygame.mouse.get_pos()):
                couleur_jouer = (255, 50, 50) if choix_grille is None and palette_couleur is None else (0, 100, 200)
            else:
                couleur_jouer = (255, 0, 0) if choix_grille is None or palette_couleur is None else (0, 150, 255)

            pygame.draw.rect(screen, couleur_jouer, bouton_jouer, border_radius=10)
            texte_jouer = font.render("Jouer", True, blanc)
            screen.blit(texte_jouer, (bouton_jouer.x + (bouton_jouer.width - texte_jouer.get_width()) // 2, bouton_jouer.y + (bouton_jouer.height - texte_jouer.get_height()) // 2))

            pygame.display.flip()

            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for rect, taille in boutons:
                        if rect.collidepoint(event.pos):
                            choix_grille = taille  # Sélectionne la grille
                    for rect, palette in boutons2:
                        if rect.collidepoint(event.pos):
                            palette_couleur = palette
                    if bouton_jouer.collidepoint(event.pos) and choix_grille is not None and palette_couleur is not None :
                        taille_piece = 480//choix_grille
                        scene = 2
                        fichier = "Grille" + str(choix_grille) + "x" + str(choix_grille) + ".txt" #A modifier en fonction de choix_grille
                        taille_grille, nombre_couleurs, grille = lire_fichier(fichier)

                        couleurs = generer_couleurs(nombre_couleurs,palette_couleur)
                        pieces = creer_pieces(grille, couleurs)
                        modification_style(palette_couleur)

                        run = False# Quitte le menu et lance le jeu

    ##

    if scene == 2 :

        # Gestion des événements
        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # Quitter
                running = False

            # Sélectionner une pièce avec la souris
            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:  # Clic gauche pour déplacer
                    for piece in pieces:
                        if piece.rect.collidepoint(event.pos):
                            selected_tile = piece

                            if (piece.colonne, piece.ligne) in grille_jeu:  # Si elle était placée
                                grille_jeu.pop((piece.colonne, piece.ligne), None)
                                piece.colonne, piece.ligne = None, None  # La rendre libre
                                #print(grille_jeu)


                elif event.button == 3:  # Clic droit pour pivoter
                    for piece in pieces:
                        if piece.rect.collidepoint(event.pos):
                            if (piece.colonne, piece.ligne) in grille_jeu: #vérifie si la pièce est déja dans la grille
                                continue  # Ignore la tentative de rotation
                            piece.rotate()


            # Relâcher la pièce et la fixer sur la grille
            if event.type == pygame.MOUSEBUTTONUP and selected_tile:

                # Trouver la case la plus proche
                selected_tile.colonne = round((selected_tile.rect.x - x_debut) / taille_piece)
                selected_tile.ligne   = round((selected_tile.rect.y - y_debut) / taille_piece)

                # Vérifier que la pièce reste dans la zone de la grille
                if 0 <= selected_tile.colonne < choix_grille and 0 <= selected_tile.ligne < choix_grille:

                    # Vérifier si une pièce est déjà présente
                    if grille_jeu.get((selected_tile.colonne, selected_tile.ligne)) is None:
                        posable = True

                        # Vérifie si la pièce au dessus a la même couleur
                        if selected_tile.ligne != 0 and posable:
                            if grille_jeu.get((selected_tile.colonne, selected_tile.ligne - 1)) is not None:
                                if grille_jeu.get((selected_tile.colonne, selected_tile.ligne - 1)).cotes[2] == selected_tile.cotes[0]:
                                    posable = True
                                else:
                                    posable = False

                        # Vérifie si le bord est gris (haut)
                        if selected_tile.ligne == 0 and posable:
                            if selected_tile.cotes[0] == 0:
                                posable = True
                            else:
                                posable = False

                        # Vérifie si la pièce à gauche a la même couleur
                        if selected_tile.colonne != 0 and posable:
                            if grille_jeu.get((selected_tile.colonne - 1, selected_tile.ligne)) is not None:
                                if grille_jeu.get((selected_tile.colonne - 1, selected_tile.ligne)).cotes[1] == selected_tile.cotes[3]:
                                    posable = True
                                else:
                                    posable = False

                        # Vérifie si le bord est gris (gauche)
                        if selected_tile.colonne == 0 and posable:
                            if selected_tile.cotes[3] == 0:
                                posable = True
                            else:
                                posable = False

                        # Vérifie si la pièce en dessous a la même couleur
                        if selected_tile.ligne != choix_grille - 1 and posable:
                            if grille_jeu.get((selected_tile.colonne, selected_tile.ligne + 1)) is not None:
                                if grille_jeu.get((selected_tile.colonne, selected_tile.ligne + 1)).cotes[0] == selected_tile.cotes[2]:
                                    posable = True
                                else:
                                    posable = False

                        # Vérifie si le bord est gris (bas)
                        if selected_tile.ligne == choix_grille - 1 and posable:
                            if selected_tile.cotes[2] == 0:
                                posable = True
                            else:
                                posable = False

                        # Vérifie si la pièce à droite a la même couleur
                        if selected_tile.colonne != choix_grille - 1 and posable:
                            if grille_jeu.get((selected_tile.colonne + 1, selected_tile.ligne)) is not None:
                                if grille_jeu.get((selected_tile.colonne + 1, selected_tile.ligne)).cotes[3] == selected_tile.cotes[1]:
                                    posable = True
                                else:
                                    posable = False

                        # Vérifie si le bord est gris (droite)
                        if selected_tile.colonne == choix_grille - 1 and posable:
                            if selected_tile.cotes[1] == 0:
                                posable = True
                            else:
                                posable = False

                        # Si toutes les conditions sont vérifiées
                        if posable:
                            selected_tile.rect.x = x_debut + selected_tile.colonne * taille_piece
                            selected_tile.rect.y = y_debut + selected_tile.ligne * taille_piece

                            grille_jeu[(selected_tile.colonne, selected_tile.ligne)] = selected_tile  # Ajouter au dictionnaire

                        # Sinon, replacer la pièce aléatoirement dans le tas
                        else:
                            selected_tile.rect.x = random.randint(650, largeur_screen - (taille_piece + 50 + (largeur_screen-x_debut_regles)))
                            selected_tile.rect.y = random.randint(185, longueur_screen - (taille_piece + 50))

                            selected_tile.colonne = None
                            selected_tile.ligne = None

                    else:
                        # Si une pièce est déjà présente, replacer la pièce aléatoirement
                        selected_tile.rect.x = random.randint(650, largeur_screen - (taille_piece + 50 + (largeur_screen-x_debut_regles)))
                        selected_tile.rect.y = random.randint(185, longueur_screen - (taille_piece + 50))

                        selected_tile.colonne = None
                        selected_tile.ligne = None

                else:
                    # Si hors de la grille, replacer dans le tas
                    selected_tile.colonne = None
                    selected_tile.ligne = None

                selected_tile = None  # Désélectionner la pièce



            # Déplacer une pièce sélectionnée
            if event.type == pygame.MOUSEMOTION and selected_tile:
                selected_tile.rect.x, selected_tile.rect.y = event.pos

                # Empêcher de dépasser à gauche et à droite de la fenêtre
                selected_tile.rect.x = max(0, min(selected_tile.rect.x, largeur_screen - taille_piece))

                # Empêcher de dépasser en haut et en bas de la fenêtre
                selected_tile.rect.y = max(0, min(selected_tile.rect.y, longueur_screen - taille_piece))

        draw_ecran()

        # Dessiner les pièces
        for piece in pieces:
            piece.draw(screen)

        if len(grille_jeu) == choix_grille**2: #Vérifie si toutes les pièces sont dans la grille
            font = pygame.font.Font(None, 74)
            texte = font.render("Félicitations !", True, (0, 255, 0))
            screen.blit(texte, (largeur_screen // 2 - texte.get_width() // 2, longueur_screen // 2 - texte.get_height() // 2))
            pygame.display.flip()
            time.sleep(5)  # Pause pour que le joueur voie le message
            running = False  # Terminer le jeu


        pygame.display.flip()


pygame.quit()




