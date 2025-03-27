from piece import Piece

class Noeud:
    def __init__(self, grille, pieces_a_placer, parent=None):
        self.grille = grille  # État actuel de la grille, un dictionnaire avec des tuples (ligne, colonne) comme clés
        self.pieces_a_placer = pieces_a_placer  # Liste des pièces à placer
        self.parent = parent  # Référence au noeud parent

    def est_solution(self):
        # Vérifie si ce noeud représente une solution complète
        return len(self.pieces_a_placer) == 0

    def generer_enfants(self):
        enfants = []
        # Trouver la case libre de plus petit index
        position_libre = self.trouver_case_libre()

        if position_libre is None:
            print("Aucune case libre trouvée.")
            return enfants

        print(f"Case libre trouvée à la position {position_libre}.")

        # Pour chaque pièce possible
        for piece in self.pieces_a_placer:
            # Réinitialiser la rotation de la pièce
            piece.rotation_index = 0
            # Pour chaque rotation possible de la pièce
            for rotation in range(4):  # Supposons 4 rotations possibles
                nouvelle_grille = self.placer_piece(piece, position_libre)
                if nouvelle_grille:
                    nouvelles_pieces = self.pieces_a_placer[:]
                    nouvelles_pieces.remove(piece)
                    enfant = Noeud(nouvelle_grille, nouvelles_pieces, self)
                    enfants.append(enfant)

        return enfants

    def trouver_case_libre(self):
        # Trouver la case libre de plus petit index
        for ligne in range(int(len(self.grille) ** 0.5)):
            for colonne in range(int(len(self.grille) ** 0.5)):
                if (ligne, colonne) not in self.grille or self.grille[(ligne, colonne)] is None:
                    return (ligne, colonne)
        return None

    def placer_piece(self, piece, position):
        # Logique pour placer la pièce dans la grille avec la rotation donnée
        nouvelle_grille = self.grille.copy()
        # Appliquer la rotation à la pièce
        piece.rotate()
        # Placer la pièce dans la grille
        if self.respecte_regle(piece, position, nouvelle_grille):
            nouvelle_grille[position] = piece
            print(f"Pièce placée à la position {position}.")
            return nouvelle_grille
        print(f"Impossible de placer la pièce à la position {position}.")
        return None

    def respecte_regle(self, piece, position, nouvelle_grille):
        # Vérifie si la pièce respecte les règles du jeu à la position donnée
        ligne, colonne = position

        print(f"Vérification des règles pour la pièce à la position {position} (ligne {ligne}, colonne {colonne}).")

        # Vérifie si la pièce au-dessus a la même couleur
        if ligne != 0:
            if (ligne - 1, colonne) in nouvelle_grille and nouvelle_grille[(ligne - 1, colonne)] is not None:
                if nouvelle_grille[(ligne - 1, colonne)].cotes[2] != piece.cotes[0]:
                    print("Règle violée : pièce au-dessus.")
                    return False

        # Vérifie si le bord est gris (haut)
        if ligne == 0:
            if piece.cotes[0] != 0:
                print("Règle violée : bord gris (haut).")
                return False

        # Vérifie si la pièce à gauche a la même couleur
        if colonne != 0:
            if (ligne, colonne - 1) in nouvelle_grille and nouvelle_grille[(ligne, colonne - 1)] is not None:
                if nouvelle_grille[(ligne, colonne - 1)].cotes[1] != piece.cotes[3]:
                    print("Règle violée : pièce à gauche.")
                    return False

        # Vérifie si le bord est gris (gauche)
        if colonne == 0:
            if piece.cotes[3] != 0:
                print("Règle violée : bord gris (gauche).")
                return False

        # Vérifie si la pièce en dessous a la même couleur
        if ligne != int(len(nouvelle_grille) ** 0.5) - 1:
            if (ligne + 1, colonne) in nouvelle_grille and nouvelle_grille[(ligne + 1, colonne)] is not None:
                if nouvelle_grille[(ligne + 1, colonne)].cotes[0] != piece.cotes[2]:
                    print("Règle violée : pièce en dessous.")
                    return False

        # Vérifie si le bord est gris (bas)
        if ligne == int(len(nouvelle_grille) ** 0.5) - 1:
            if piece.cotes[2] != 0:
                print("Règle violée : bord gris (bas).")
                return False

        # Vérifie si la pièce à droite a la même couleur
        if colonne != int(len(nouvelle_grille) ** 0.5) - 1:
            if (ligne, colonne + 1) in nouvelle_grille and nouvelle_grille[(ligne, colonne + 1)] is not None:
                if nouvelle_grille[(ligne, colonne + 1)].cotes[3] != piece.cotes[1]:
                    print("Règle violée : pièce à droite.")
                    return False

        # Vérifie si le bord est gris (droite)
        if colonne == int(len(nouvelle_grille) ** 0.5) - 1:
            if piece.cotes[1] != 0:
                print("Règle violée : bord gris (droite).")
                return False

        print("Toutes les règles respectées.")
        return True
