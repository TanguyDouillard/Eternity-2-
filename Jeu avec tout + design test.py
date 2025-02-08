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


#Création de l'écran (fond, grille etc...)
def draw_ecran():
    global choix_grille, taille_piece

    x_debut, y_debut = 50, 200
    screen.fill("lightblue")  # Effacer l'écran

    # Dessiner la grille
    pygame.draw.rect(screen, (127, 140, 141), (35, 185, 510, 510))  # Fond de la grille en gris

    for j in range(choix_grille**2):
        i = j
        if j % choix_grille == 0 and j != 0:
            y_debut += taille_piece
        if j >= choix_grille:
            i = i % choix_grille

        pygame.draw.rect(screen, "black", ((x_debut + (i * taille_piece)), y_debut, taille_piece, taille_piece))
        pygame.draw.rect(screen, "white", ((x_debut + (i * taille_piece)), y_debut, taille_piece, taille_piece), width=1)

    # Titre "Eternity II"
    try:
        font_titre = pygame.font.Font("Orbitron/Orbitron-Regular.ttf", 100)
    except:
        font_titre = pygame.font.Font(None, 100)

    texte_titre = font_titre.render("Eternity II", True, "black")
    screen.blit(texte_titre, (largeur_screen // 2 - texte_titre.get_width() // 2, 70 - texte_titre.get_height() // 2))

    # Affichage du logo
    screen.blit(logo, (10, 10))

    # ITRE "RÈGLES"
    try:
        font_titre_regles = pygame.font.Font("Orbitron/Orbitron-Regular.ttf", 30)
    except:
        font_titre_regles = pygame.font.Font(None, 35)

    titre_regles = font_titre_regles.render("RÈGLES", True, (0, 0, 0))  # Noir
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
Les bords de la grille doivent
être gris.

Commandes :
- Clic gauche : déplacer une pièce
- Clic droit : faire pivoter une pièce

Bonne chance !"""

    # Définition de la zone d'affichage
    rect_zone = pygame.Rect(x_debut_regles, y_debut_regles, 375, 520)  # Hauteur ajustée
    couleur_fond = (220, 220, 220)  # Gris clair

    # Police et taille du texte
    try:
        font_regles = pygame.font.Font("Orbitron/Orbitron-Regular.ttf", 20)
    except:
        font_regles = pygame.font.Font(None, 25)

    # Affichage du fond de la zone
    pygame.draw.rect(screen, couleur_fond, rect_zone, border_radius=10)  # Bord arrondi

    # Découper et afficher le texte proprement
    lignes = texte_regles.split("\n")  # Séparer les lignes avec "\n"
    y = rect_zone.top + 10  # Décalage du haut

    for ligne in lignes:
        if ligne.strip() == "":  # Vérifier si la ligne est vide pour ajouter un espace vertical
            y += font_regles.get_height() // 2
        else:
            texte_render = font_regles.render(ligne, True, (0, 0, 0))  # Noir
            screen.blit(texte_render, (rect_zone.left + 5, y))
            y += font_regles.get_height()

    # Afficher le contour du rectangle
    pygame.draw.rect(screen, (100, 100, 100), rect_zone, width=2, border_radius=10)

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
def generer_couleurs(nombre_couleurs):
    couleurs_bases = {
   0:(127, 140, 141),  # Gris
   1:(255, 87, 51),    # Rouge vif
   2:(51, 255, 87),    # Vert vif
   3:(51, 87, 255),    # Bleu vif
   4:(241, 196, 15),   # Jaune
   5:(142, 68, 173),   # Violet
   6:(26, 188, 156),   # Turquoise
   7:(231, 76, 60),    # Rouge tomate
   8:(46, 204, 113),   # Vert émeraude
   9:(52, 152, 219),   # Bleu clair
   10:(230, 126, 34),   # Orange vif
   11:(155, 89, 182),   # Mauve
   12:(52, 73, 94),     # Bleu gris
   13:(22, 160, 133),   # Vert océan
   14:(192, 57, 43),    # Rouge brique
   15:(41, 128, 185),   # Bleu profond
   16:(39, 174, 96),    # Vert forêt
   17:(243, 156, 18),   # Orange doré
   18:(211, 84, 0),     # Orange foncé
   19:(189, 195, 199),  # Gris clair
   20:(149, 165, 166),  # Gris bleuté
   21:(44, 62, 80),     # Bleu nuit
   22:(236, 240, 241)   # Blanc cassé
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

couleurs = generer_couleurs(nombre_couleurs)
pieces = creer_pieces(grille, couleurs)


#Création dictionnaire pour vérifier si case pleine ou pas
grille_jeu = {}  # Dictionnaire vide


#La pièce sélectionnée par l'utlisateur
selected_tile = None


###############################


#Boucle

while running:

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

                        # Sauvegarde temporaire de l'ancienne position au cas où
                        old_colonne, old_ligne = piece.colonne, piece.ligne

                        if (piece.colonne, piece.ligne) in grille_jeu:  # Si la pièce était posée
                            print(f"🔴 Suppression de ({piece.colonne}, {piece.ligne}) du dico")  # DEBUG
                            grille_jeu.pop((piece.colonne, piece.ligne), None)
                            piece.colonne, piece.ligne = None, None  # La rendre libre
                            print(f"📌 Après sélection, grille_jeu contient : {grille_jeu.keys()}")  # DEBUG


            elif event.button == 3:  # Clic droit pour pivoter
                for piece in pieces:
                    if piece.rect.collidepoint(event.pos):
                        if (piece.colonne, piece.ligne) in grille_jeu: #vérifie si la pièce est déja dans la grille
                            continue  # Ignore la tentative de rotation
                        piece.rotate()


        # Relâcher la pièce et la fixer sur la grille


        # Relâcher la pièce et la fixer sur la grille
        if event.type == pygame.MOUSEBUTTONUP and selected_tile:
            # Trouver la case la plus proche
            selected_tile.colonne = round((selected_tile.rect.x - x_debut) / taille_piece)
            selected_tile.ligne   = round((selected_tile.rect.y - y_debut) / taille_piece)

            if 0 <= selected_tile.colonne < choix_grille and 0 <= selected_tile.ligne < choix_grille:
                # Vérifier si la case est déjà occupée
                if (selected_tile.colonne, selected_tile.ligne) in grille_jeu:
                    print(f"⚠️ La case ({selected_tile.colonne}, {selected_tile.ligne}) est déjà occupée.")
                    posable = False
                else:
                    posable = True

                    # Vérification des bords et des pièces adjacentes...

                    # 2️⃣ Vérifier si les bords sont corrects AVANT de poser
                    # 🔹 Vérifie si le haut correspond
                    if selected_tile.ligne > 0:  # Pas de vérif si on est au bord
                        piece_au_dessus = grille_jeu.get((selected_tile.colonne, selected_tile.ligne - 1))
                        if piece_au_dessus and piece_au_dessus.cotes[2] != selected_tile.cotes[0]:
                            posable = False

                    # 🔹 Vérifie si la gauche correspond
                    if selected_tile.colonne > 0:
                        piece_a_gauche = grille_jeu.get((selected_tile.colonne - 1, selected_tile.ligne))
                        if piece_a_gauche and piece_a_gauche.cotes[1] != selected_tile.cotes[3]:
                            posable = False

                    # 🔹 Vérifie si le bas correspond
                    if selected_tile.ligne < choix_grille - 1:
                        piece_en_dessous = grille_jeu.get((selected_tile.colonne, selected_tile.ligne + 1))
                        if piece_en_dessous and piece_en_dessous.cotes[0] != selected_tile.cotes[2]:
                            posable = False

                    # 🔹 Vérifie si la droite correspond
                    if selected_tile.colonne < choix_grille - 1:
                        piece_a_droite = grille_jeu.get((selected_tile.colonne + 1, selected_tile.ligne))
                        if piece_a_droite and piece_a_droite.cotes[3] != selected_tile.cotes[1]:
                            posable = False

                    # 3️⃣ Vérification des bords gris
                    if selected_tile.ligne == 0 and selected_tile.cotes[0] != 0:  # Bord haut
                        posable = False
                    if selected_tile.colonne == 0 and selected_tile.cotes[3] != 0:  # Bord gauche
                        posable = False
                    if selected_tile.ligne == choix_grille - 1 and selected_tile.cotes[2] != 0:  # Bord bas
                        posable = False
                    if selected_tile.colonne == choix_grille - 1 and selected_tile.cotes[1] != 0:  # Bord droit
                        posable = False

                # Si toutes les conditions sont OK, on place la pièce
                if posable:
                    selected_tile.rect.x = x_debut + selected_tile.colonne * taille_piece
                    selected_tile.rect.y = y_debut + selected_tile.ligne * taille_piece
                    grille_jeu[(selected_tile.colonne, selected_tile.ligne)] = selected_tile
                    print(f"✅ Pièce placée à ({selected_tile.colonne}, {selected_tile.ligne})")
                else:
                    print(f"⚠️ Impossible de placer en ({selected_tile.colonne}, {selected_tile.ligne})")

            selected_tile = None  # Déselectionner la pièce












##
##        if event.type == pygame.MOUSEBUTTONUP and selected_tile:
##
##
##            # Trouver la case la plus proche
##            selected_tile.colonne = round((selected_tile.rect.x - x_debut) / taille_piece)
##            selected_tile.ligne   = round((selected_tile.rect.y - y_debut) / taille_piece)
##
##            print(f"🔵 Tentative de placement en ({selected_tile.colonne}, {selected_tile.ligne})")  # DEBUG
##
##            # Vérifier que la pièce reste dans la zone de la grille
##            if 0 <= selected_tile.colonne < choix_grille and 0 <= selected_tile.ligne < choix_grille:
##
##                # 1️⃣ Vérifier que la case est libre avant toute autre chose
##                if grille_jeu.get((selected_tile.colonne, selected_tile.ligne)) is None:
##                    posable = True
##
##                    # 2️⃣ Vérifier si les bords sont corrects AVANT de poser
##                    # 🔹 Vérifie si le haut correspond
##                    if selected_tile.ligne > 0:  # Pas de vérif si on est au bord
##                        piece_au_dessus = grille_jeu.get((selected_tile.colonne, selected_tile.ligne - 1))
##                        if piece_au_dessus and piece_au_dessus.cotes[2] != selected_tile.cotes[0]:
##                            posable = False
##
##                    # 🔹 Vérifie si la gauche correspond
##                    if selected_tile.colonne > 0:
##                        piece_a_gauche = grille_jeu.get((selected_tile.colonne - 1, selected_tile.ligne))
##                        if piece_a_gauche and piece_a_gauche.cotes[1] != selected_tile.cotes[3]:
##                            posable = False
##
##                    # 🔹 Vérifie si le bas correspond
##                    if selected_tile.ligne < choix_grille - 1:
##                        piece_en_dessous = grille_jeu.get((selected_tile.colonne, selected_tile.ligne + 1))
##                        if piece_en_dessous and piece_en_dessous.cotes[0] != selected_tile.cotes[2]:
##                            posable = False
##
##                    # 🔹 Vérifie si la droite correspond
##                    if selected_tile.colonne < choix_grille - 1:
##                        piece_a_droite = grille_jeu.get((selected_tile.colonne + 1, selected_tile.ligne))
##                        if piece_a_droite and piece_a_droite.cotes[3] != selected_tile.cotes[1]:
##                            posable = False
##
##                    # 3️⃣ Vérification des bords gris
##                    if selected_tile.ligne == 0 and selected_tile.cotes[0] != 0:  # Bord haut
##                        posable = False
##                    if selected_tile.colonne == 0 and selected_tile.cotes[3] != 0:  # Bord gauche
##                        posable = False
##                    if selected_tile.ligne == choix_grille - 1 and selected_tile.cotes[2] != 0:  # Bord bas
##                        posable = False
##                    if selected_tile.colonne == choix_grille - 1 and selected_tile.cotes[1] != 0:  # Bord droit
##                        posable = False
##
##                    # 4️⃣ Si toutes les conditions sont OK, on place la pièce
##                    if posable:
##                        selected_tile.rect.x = x_debut + selected_tile.colonne * taille_piece
##                        selected_tile.rect.y = y_debut + selected_tile.ligne * taille_piece
##                        grille_jeu[(selected_tile.colonne, selected_tile.ligne)] = selected_tile  # Ajouter au dictionnaire
##
##                        print(f"✅ Pièce placée à ({selected_tile.colonne}, {selected_tile.ligne})")  # DEBUG
##
##                    if not posable:  # Si elle ne peut pas être placée
##                        print(f"⚠️ Impossible de placer en ({selected_tile.colonne}, {selected_tile.ligne})")  # DEBUG
##
##                        if old_colonne is not None and old_ligne is not None:
##                            # Remettre la pièce là où elle était avant d'être déplacée
##                            selected_tile.rect.x = x_debut + old_colonne * taille_piece
##                            selected_tile.rect.y = y_debut + old_ligne * taille_piece
##                            grille_jeu[(old_colonne, old_ligne)] = selected_tile  # La remettre dans le dictionnaire
##                        else:
##                            # Sinon, replacer dans le tas aléatoirement
##                            selected_tile.rect.x = random.randint(650, largeur_screen - (taille_piece + 50 + (largeur_screen - x_debut_regles)))
##                            selected_tile.rect.y = random.randint(185, longueur_screen - (taille_piece + 50))
##
##            selected_tile = None  # Déselectionner la pièce


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













