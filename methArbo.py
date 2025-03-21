from noeud import Noeud
from listeNoeud import ListeNoeud
import threading
import time


def run_ia():
    global grille_jeu, pieces, ia_running, choix_grille, taille_piece

    # Initialisation de l'IA
    ia_running = True

    # Créer le noeud initial
    noeud_initial = Noeud(grille_jeu, pieces)

    # Explorer l'arborescence
    solution = explorer_profondeur(noeud_initial)

    # Si une solution est trouvée, mettre à jour l'affichage
    if solution:
        grille_jeu = solution.grille
        pieces = solution.pieces_a_placer
        draw_ecran()
        for piece in pieces:
            piece.draw(screen)
        pygame.display.flip()

    # Arrêter l'IA
    ia_running = False


def explorer_profondeur(noeud_initial):
    liste_noeuds = ListeNoeud()
    liste_noeuds.ajouter_noeud(noeud_initial)

    while liste_noeuds:
        noeud_courant = liste_noeuds.obtenir_dernier_noeud()
        if noeud_courant is None:
            break

        if noeud_courant.est_solution():
            return noeud_courant  # Solution trouvée

        enfants = noeud_courant.generer_enfants()
        for enfant in enfants:
            if not liste_noeuds.contient_noeud(enfant):
                liste_noeuds.ajouter_noeud(enfant)

    return None  # Aucune solution trouvée
