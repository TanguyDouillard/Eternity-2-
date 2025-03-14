import pygame
import random
import time

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur_screen,longueur_screen = 1200 , 700
screen = pygame.display.set_mode((largeur_screen, longueur_screen))
pygame.display.set_caption("Eternity ii")



choix_grille = random.choice([4,6,8,12,16]) #A modifier en fonction du choix de l'utilisateur !
print(choix_grille)
taille_piece = 480//choix_grille
x_debut , y_debut = 50,100 #Pour le point en haut à gauche de la grille

#Création de l'écran (fond, grille etc...)
def draw_ecran():
    global choix_grille,taille_piece

    x_debut , y_debut = 50,100

    screen.fill("lightblue")  # Effacer l'écran

    pygame.draw.rect(screen, "grey", (35, 85, 510, 510))
    #pygame.draw.rect(screen, "green", (50, 100, 480, 480))

    for j in range(choix_grille**2):

        i=j

        if j%choix_grille == 0 and j != 0:
            y_debut += taille_piece

        if j >= choix_grille :
            i = i%choix_grille

        pygame.draw.rect(screen,"black",((x_debut + (i*(taille_piece))), y_debut , taille_piece , taille_piece))
        pygame.draw.rect(screen,"white",((x_debut + (i*(taille_piece))), y_debut , taille_piece , taille_piece), width=1)
        #print(i," :  ",(x_debut + (i*(taille_piece))), y_debut , taille_piece , taille_piece)


###########################################

#Créer pièces
class Piece:
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

    def rotate(self):
        # Rotation de 90 degrés (changer l'ordre des bords)
        self.couleurs = self.couleurs[-1:] + self.couleurs[:-1]
        self.cotes = self.cotes[-1:] + self.cotes[:-1]
        self.rotation = (self.rotation + 90) % 360

    def draw(self, surface):
        # Dessiner la pièce avec ses triangles colorés
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


def lire_fichier(filename):
    with open(filename, 'r') as f:
        taille_grille, nombre_couleurs = map(int, f.readline().strip().split())
        grille = []
        for ligne in f:
            piece = tuple(map(int, ligne.strip().strip('()').split(',')))
            grille.append(piece)
    return taille_grille, nombre_couleurs, grille

def generer_couleurs(nombre_couleurs):
    # Assigner des couleurs fixes aux chiffres
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

def creer_pieces(grille, couleurs):
    pieces = []
    for i, cotes in enumerate(grille):
        couleurs_piece = [
            couleurs[cotes[0]],  # Haut
            couleurs[cotes[1]],  # Droite
            couleurs[cotes[2]],  # Bas
            couleurs[cotes[3]],  # Gauche
        ]
        piece = Piece(i, random.randint(650, 1200 - (130 + 50)), random.randint(100, 700 - (130 + 50)), cotes, couleurs_piece)  # Par défaut, aucune position
        pieces.append(piece)
    return pieces

#Boucle run
running = True
fichier = "Grille" + str(choix_grille) + "x" + str(choix_grille) + ".txt" #A modifier en fonction de choix_grille
selected_tile = None

taille_grille, nombre_couleurs, grille = lire_fichier(fichier)

couleurs = generer_couleurs(nombre_couleurs)
pieces = creer_pieces(grille, couleurs)

##Création dictionnaire pour vérifier si case pleine ou pas
grille_jeu = {}  # Dictionnaire vide


while running:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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

        # Relâcher la pièce
##        if event.type == pygame.MOUSEBUTTONUP and selected_tile:
##            selected_tile = None
        # Relâcher la pièce et la fixer sur la grille
        if event.type == pygame.MOUSEBUTTONUP and selected_tile:
            # Trouver la case la plus proche
##            grid_x = round((selected_tile.rect.x - x_debut) / taille_piece)
##            grid_y = round((selected_tile.rect.y - y_debut) / taille_piece)
##
##            print("selected_tile.rect.y : ",selected_tile.rect.y, "   y_debut : ", y_debut, "colonne : ", (selected_tile.rect.y - y_debut) / taille_piece)
##            print("x : ",grid_x, "    y : ", grid_y)

            selected_tile.colonne = round((selected_tile.rect.x - x_debut) / taille_piece)
            selected_tile.ligne   = round((selected_tile.rect.y - y_debut) / taille_piece)


            # Vérifier que la pièce reste dans la zone de la grille
            if 0 <= selected_tile.colonne < choix_grille and 0 <= selected_tile.ligne < choix_grille and grille_jeu.get((selected_tile.colonne,selected_tile.ligne)) is None:
                posable = True

                if selected_tile.ligne != 0 and posable:
                    if grille_jeu.get((selected_tile.colonne,selected_tile.ligne - 1)) is not None :
                        if grille_jeu.get((selected_tile.colonne,selected_tile.ligne - 1)).cotes[2] == selected_tile.cotes[0]:
                            posable = True
                        else:
                            posable = False
                    
                if selected_tile.ligne == 0 and posable :
                    if selected_tile.cotes[0]==0:
                        posable = True
                    else:
                        posable = False

                print(posable)

                if selected_tile.colonne != 0 and posable :
                    if grille_jeu.get((selected_tile.colonne - 1,selected_tile.ligne)) is not None :
                        if grille_jeu.get((selected_tile.colonne - 1,selected_tile.ligne)).cotes[1] == selected_tile.cotes[3]:
                            posable = True
                        else:
                            posable = False
                
                if selected_tile.colonne == 0 and posable :
                    if selected_tile.cotes[3]==0:
                        posable = True
                    else:
                        posable = False
                    
                
                
                print(posable)

                if selected_tile.ligne != choix_grille-1 and posable:
                    if grille_jeu.get((selected_tile.colonne,selected_tile.ligne + 1)) is not None :
                        if grille_jeu.get((selected_tile.colonne,selected_tile.ligne + 1)).cotes[0] == selected_tile.cotes[2]:
                            posable = True
                        else:
                            posable = False
                            
                if selected_tile.ligne == choix_grille-1 and posable :
                    if selected_tile.cotes[2]==0:
                        posable = True
                    else:
                        posable = False

                print(posable)

                if selected_tile.colonne != choix_grille-1 and posable :
                    if grille_jeu.get((selected_tile.colonne + 1,selected_tile.ligne)) is not None :
                        if grille_jeu.get((selected_tile.colonne + 1,selected_tile.ligne)).cotes[3] == selected_tile.cotes[1]:
                            posable = True
                        else:
                            posable = False
                            
                if selected_tile.colonne == choix_grille-1 and posable :
                    if selected_tile.cotes[1]==0:
                        posable = True
                    else:
                        posable = False

                print(posable)


                if posable == True:
                    selected_tile.rect.x = x_debut + selected_tile.colonne * taille_piece
                    selected_tile.rect.y = y_debut + selected_tile.ligne * taille_piece

                    grille_jeu[(selected_tile.colonne, selected_tile.ligne)] = selected_tile #On l'ajoute au dico

                else:
                # Si hors grille, la replacer à sa position initiale (ou autre logique)
                    selected_tile.rect.x = random.randint(650, 1200 - (130 + 50))
                    selected_tile.rect.y = random.randint(100, 700 - (130 + 50))


            else:
                # Si hors grille, la replacer à sa position initiale (ou autre logique)
                selected_tile.rect.x = random.randint(650, 1200 - (130 + 50))
                selected_tile.rect.y = random.randint(100, 700 - (130 + 50))

            selected_tile = None  # Déselectionner la pièce


        # Déplacer une pièce sélectionnée
        if event.type == pygame.MOUSEMOTION and selected_tile:
            selected_tile.rect.x, selected_tile.rect.y = event.pos


    draw_ecran()

    # Dessiner les pièces
    for piece in pieces:
        piece.draw(screen)

    pygame.display.flip()


pygame.quit()













