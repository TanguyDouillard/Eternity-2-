import pygame
import time
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
largeur = 1200
longueur = 700
screen = pygame.display.set_mode((largeur, longueur))
pygame.display.set_caption("Eternity ii")

screen.fill("lightblue")

#Création grille puzzle
largeur_grille,longueur_grille = 600,600
pygame.draw.rect(screen,"green",(50,100,520,520))
pygame.draw.line(screen,"black",(180,100),(180,620))
pygame.draw.line(screen,"black",(310,100),(310,620))
pygame.draw.line(screen,"black",(440,100),(440,620))
pygame.draw.line(screen,"black",(50,230),(570,230))
pygame.draw.line(screen,"black",(50,360),(570,360))
pygame.draw.line(screen,"black",(50,490),(570,490))
pygame.display.update()


COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (128, 128, 128)]  # Rouge, Vert, Bleu, Jaune, Gris
BLACK = (0, 0, 0)

TILE_SIZE = 150 #car 600/4
#Création pièces
class Tile:
    def __init__(self, x, y, edges):
        self.x = x
        self.y = y
        self.edges = edges  # Haut, Droite, Bas, Gauche
        self.rotation = 0  # Rotation actuelle (0, 90, 180, 270)
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)

    def rotate(self):
        # Rotation de 90 degrés (changer l'ordre des bords)
        self.edges = self.edges[-1:] + self.edges[:-1]
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
        pygame.draw.polygon(surface, self.edges[0], [corners[0], corners[1], (cx, cy)])
        # Triangle droit
        pygame.draw.polygon(surface, self.edges[1], [corners[1], corners[2], (cx, cy)])
        # Triangle bas
        pygame.draw.polygon(surface, self.edges[2], [corners[2], corners[3], (cx, cy)])
        # Triangle gauche
        pygame.draw.polygon(surface, self.edges[3], [corners[3], corners[0], (cx, cy)])

def generate_pieces():
    pieces = []
    for _ in range(4 * 4):
        edges = [random.choice(COLORS) for _ in range(4)]
        pieces.append(Tile(random.randint(650, 1200 - (150+50)), random.randint(100, 700 - (150+50)), edges))
    return pieces

pieces = generate_pieces()
selected_tile = None


test=True
while test == True:
##
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            running = False
##
##    for piece in pieces:
##        piece.draw(screen)
##
##    # Mettre à jour l'affichage
##    pygame.display.update()
##
##    time.sleep(30)
##    test=False

    # Dessiner les pièces
    for piece in pieces:
        piece.draw(screen)


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Sélectionner une pièce avec la souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic gauche pour déplacer
                for piece in pieces:
                    if piece.rect.collidepoint(event.pos):
                        selected_tile = piece
            elif event.button == 3:  # Clic droit pour pivoter
                for piece in pieces:
                    if piece.rect.collidepoint(event.pos):
                        piece.rotate()

        # Relâcher la pièce
        if event.type == pygame.MOUSEBUTTONUP and selected_tile:
            selected_tile = None

        # Déplacer une pièce sélectionnée
        if event.type == pygame.MOUSEMOTION and selected_tile:
            selected_tile.rect.x, selected_tile.rect.y = event.pos





pygame.quit()
