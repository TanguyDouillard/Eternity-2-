import pygame
from piece import Piece
import random

class Noeud:
    def __init__(self, grille, pieces_a_placer):
        self.grille = {}
        for (ligne, colonne), piece in grille.items():
            # Conversion explicite des cotes en liste si nécessaire
            cotes = list(piece.cotes) if isinstance(piece.cotes, tuple) else piece.cotes.copy()
            
            new_piece = Piece(
                id_piece=piece.id_piece,
                x=piece.rect.x,
                y=piece.rect.y,
                cotes=cotes,  # Utilise la version liste
                couleurs=piece.couleurs.copy(),  # Supposé être une liste
                taille_piece=piece.taille_piece,
                x_debut=piece.x_debut,
                y_debut=piece.y_debut
            )
            new_piece.rotation_index = piece.rotation_index
            self.grille[(ligne, colonne)] = new_piece
        
        self.pieces_a_placer = [p for p in pieces_a_placer]  # Copie superficielle
        
    def _copier_piece(self, piece):
        """Crée une copie indépendante d'une pièce"""
        return Piece(
            id_piece=piece.id_piece,
            x=piece.rect.x,
            y=piece.rect.y,
            cotes=list(piece.cotes),
            couleurs=piece.couleurs.copy(),
            taille_piece=piece.taille_piece,
            x_debut=piece.x_debut,
            y_debut=piece.y_debut
        )
        
    def est_solution(self):
        # Vérifie si ce noeud représente une solution complète
        return not self.pieces_a_placer
    
    def generer_enfants(self):
        from game import ia_stop_event
        
        enfants = []
        position_libre = self.trouver_case_libre()
        if not position_libre:
            return enfants
    
        # Mélange aléatoire des pièces à tester
        pieces_melangees = self.pieces_a_placer
        
        for piece in pieces_melangees:
            if ia_stop_event.is_set():
                return enfants
                
            rotations = (0, 1, 2, 3)
            
            for rotation in rotations:
                piece_tmp = self._copier_piece(piece)
                for _ in range(rotation):
                    piece_tmp.rotate()
                    
                if self._essayer_placer_piece(piece_tmp, position_libre):
                    nouvelles_pieces = [p for p in self.pieces_a_placer if p.id_piece != piece.id_piece]
                    enfants.append(Noeud(self._essayer_placer_piece(piece_tmp, position_libre), nouvelles_pieces))
        
        return enfants


    def trouver_case_libre(self):
        from game import choix_grille
        print(f"Grille actuelle : {self.grille}")  # Ajoutez ceci en début de fonction
    # Supposons que la grille est de taille choix_grille x choix_grille
        for ligne in range(choix_grille):  # Utilisez la taille globale de la grille
            for colonne in range(choix_grille):
                if (ligne, colonne) not in self.grille:
                    print(f"Case libre trouvée: {(ligne, colonne)}")
                    return (ligne, colonne)
        print("Aucune case libre trouvée!")
        return None  # Aucune case libre trouvée

    def placer_piece(self, piece, position):
        ligne, colonne = position
        nouvelle_grille = self.grille.copy()
    
        if self.respecte_regle(piece, position, nouvelle_grille):
            nouvelle_grille[position] = piece
            return nouvelle_grille
        return None

    def _essayer_placer_piece(self, piece, position):
        from game import choix_grille, x_debut, y_debut, taille_piece
        ligne, colonne = position
        nouvelle_grille = self.grille.copy()
        
        # Vérifier les bords de la grille
        if ligne == 0 and piece.cotes[0] != 0:  # Bord haut
            return None
        if colonne == 0 and piece.cotes[3] != 0:  # Bord gauche
            return None
        if ligne == choix_grille-1 and piece.cotes[2] != 0:  # Bord bas
            return None
        if colonne == choix_grille-1 and piece.cotes[1] != 0:  # Bord droit
            return None
        
        # Vérifier les voisins
        if ligne > 0:  # Voisin du haut
            voisin = self.grille.get((ligne-1, colonne))
            if voisin and voisin.cotes[2] != piece.cotes[0] or piece.cotes[0] == 0:
                return None
        if colonne > 0:  # Voisin de gauche
            voisin = self.grille.get((ligne, colonne-1))
            if voisin and voisin.cotes[1] != piece.cotes[3] or piece.cotes[3] == 0:
                return None
        if ligne < choix_grille-1:  # Voisin du bas
            voisin = self.grille.get((ligne+1, colonne))
            if voisin and voisin.cotes[0] != piece.cotes[2] or piece.cotes[2] == 0:
                return None
        if colonne < choix_grille-1:  # Voisin de droite
            voisin = self.grille.get((ligne, colonne+1))
            if voisin and voisin.cotes[3] != piece.cotes[1] or piece.cotes[1] == 0:
                return None
        
        # Si toutes les vérifications sont passées
        nouvelle_grille[(ligne,colonne)] = piece
        piece.rect.x = x_debut + colonne * taille_piece
        piece.rect.y = y_debut + ligne * taille_piece
        piece.colonne = colonne
        piece.ligne = ligne
        return nouvelle_grille