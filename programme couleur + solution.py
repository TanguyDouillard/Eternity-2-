import pygame

class Piece:
    def __init__(self, id_piece, cotes, couleurs, position):
        self.id_piece = id_piece
        self.cotes = cotes  # (haut, droite, bas, gauche)
        self.couleurs = couleurs  # Couleurs des côtés
        self.position = position  # (x, y) dans la grille ou None si non placé
        self.selected = False

    def draw(self, screen, taille_case, offset_x=0, offset_y=0):
        if self.position is None:
            return

        x, y = self.position[0] * taille_case + offset_x, self.position[1] * taille_case + offset_y

        # Dessiner les triangles de chaque côté
        # Haut
        pygame.draw.polygon(screen, self.couleurs[0], [(x, y), (x + taille_case, y), (x + taille_case // 2, y + taille_case // 2)])
        # Droite
        pygame.draw.polygon(screen, self.couleurs[1], [(x + taille_case, y), (x + taille_case, y + taille_case), (x + taille_case // 2, y + taille_case // 2)])
        # Bas
        pygame.draw.polygon(screen, self.couleurs[2], [(x, y + taille_case), (x + taille_case, y + taille_case), (x + taille_case // 2, y + taille_case // 2)])
        # Gauche
        pygame.draw.polygon(screen, self.couleurs[3], [(x, y), (x, y + taille_case), (x + taille_case // 2, y + taille_case // 2)])

    def contains_point(self, point, taille_case, offset_x=0, offset_y=0):
        if self.position is None:
            return False
        x, y = self.position
        rect = pygame.Rect(x * taille_case + offset_x, y * taille_case + offset_y, taille_case, taille_case)
        return rect.collidepoint(point)

    def move(self, new_position):
        self.position = new_position

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
        piece = Piece(i, cotes, couleurs_piece, None)  # Par défaut, aucune position
        pieces.append(piece)
    return pieces

def afficher_grille_pygame(taille_grille, pieces):
    pygame.init()

    # Configuration de la fenêtre
    largeur_fenetre = 1200
    hauteur_fenetre = 700
    largeur_grille = 480
    hauteur_grille = 510
    taille_case = hauteur_grille // taille_grille
    screen = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Puzzle Grille")


    # Initialiser les positions des pièces dans la zone à droite
    for i, piece in enumerate(pieces):
        piece.move((i % taille_grille, i // taille_grille))

    running = True
    selected_piece = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dessiner le fond
        screen.fill((255, 255, 255))  # Fond blanc

        # Dessiner la grille vide
        for i in range(taille_grille):
            for j in range(taille_grille):
                rect = pygame.Rect(j * taille_case, i * taille_case, taille_case, taille_case)
                pygame.draw.rect(screen, (50, 50, 50), rect, 1)  # Bordures de la grille

        # Dessiner les pièces
        for piece in pieces:
            piece.draw(screen, taille_case, offset_x=0 if piece.position[1] >= taille_grille else 0)

        pygame.display.flip()

    pygame.quit()

def main():
    fichier = "Grille4x4.txt"
    taille_grille, nombre_couleurs, grille = lire_fichier(fichier)

    print(f"Taille de la grille : {taille_grille}x{taille_grille}")
    print(f"Nombre de couleurs : {nombre_couleurs}")

    couleurs = generer_couleurs(nombre_couleurs)
    pieces = creer_pieces(grille, couleurs)

    afficher_grille_pygame(taille_grille, pieces)

if __name__ == "__main__":
    main()
