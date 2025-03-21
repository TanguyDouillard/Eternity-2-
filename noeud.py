from piece import Piece

class Noeud:
    def __init__(self, grille, pieces_a_placer, parent=None):
        self.grille = grille  # État actuel de la grille
        self.pieces_a_placer = pieces_a_placer  # Liste des pièces à placer
        self.parent = parent  # Référence au noeud parent

    def est_solution(self):
        # Vérifie si ce noeud représente une solution complète
        return len(self.pieces_a_placer) == 0

    def generer_enfants(self):
        enfants = []
        # Trouver la case libre de plus petit index
        index_libre = self.trouver_case_libre()

        # Pour chaque pièce possible
        for piece in self.pieces_a_placer:
            # Réinitialiser la rotation de la pièce
            piece.rotation_index = 0
            # Pour chaque rotation possible de la pièce
            for rotation in range(4):  # Supposons 4 rotations possibles
                nouvelle_grille = self.placer_piece(piece, index_libre)
                if nouvelle_grille:
                    nouvelles_pieces = self.pieces_a_placer[:]
                    nouvelles_pieces.remove(piece)
                    enfant = Noeud(nouvelle_grille, nouvelles_pieces, self)
                    enfants.append(enfant)

        return enfants

    def trouver_case_libre(self):
        # Trouver la case libre de plus petit index
        for index, case in enumerate(self.grille):
            if case is None:
                return index
        return None

    def placer_piece(self, piece, index):
        # Logique pour placer la pièce dans la grille avec la rotation donnée
        nouvelle_grille = self.grille[:]
        # Appliquer la rotation à la pièce
        piece.rotate()
        # Placer la pièce dans la grille
        if self.respecte_regle(piece, index):
            nouvelle_grille[index] = piece
            return nouvelle_grille
        return None

    def respecte_regle(self, piece, index, nouvelle_grille):
        # Vérifie si la pièce respecte les règles du jeu à l'index donné
        ligne = index // len(nouvelle_grille[0])
        colonne = index % len(nouvelle_grille[0])

        # Vérifie si la pièce au-dessus a la même couleur
        if ligne != 0:
            if nouvelle_grille[ligne - 1][colonne] is not None:
                if nouvelle_grille[ligne - 1][colonne].cotes[2] != piece.cotes[0]:
                    return False

        # Vérifie si le bord est gris (haut)
        if ligne == 0:
            if piece.cotes[0] != 0:
                return False

        # Vérifie si la pièce à gauche a la même couleur
        if colonne != 0:
            if nouvelle_grille[ligne][colonne - 1] is not None:
                if nouvelle_grille[ligne][colonne - 1].cotes[1] != piece.cotes[3]:
                    return False

        # Vérifie si le bord est gris (gauche)
        if colonne == 0:
            if piece.cotes[3] != 0:
                return False

        # Vérifie si la pièce en dessous a la même couleur
        if ligne != len(nouvelle_grille) - 1:
            if nouvelle_grille[ligne + 1][colonne] is not None:
                if nouvelle_grille[ligne + 1][colonne].cotes[0] != piece.cotes[2]:
                    return False

        # Vérifie si le bord est gris (bas)
        if ligne == len(nouvelle_grille) - 1:
            if piece.cotes[2] != 0:
                return False

        # Vérifie si la pièce à droite a la même couleur
        if colonne != len(nouvelle_grille[0]) - 1:
            if nouvelle_grille[ligne][colonne + 1] is not None:
                if nouvelle_grille[ligne][colonne + 1].cotes[3] != piece.cotes[1]:
                    return False

        # Vérifie si le bord est gris (droite)
        if colonne == len(nouvelle_grille[0]) - 1:
            if piece.cotes[1] != 0:
                return False

        return True