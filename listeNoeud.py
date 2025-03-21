from noeud import Noeud

class ListeNoeud:
    def __init__(self):
        self.noeuds = []

    def ajouter_noeud(self, noeud):
        self.noeuds.append(noeud)

    def supprimer_noeud(self, noeud):
        self.noeuds.remove(noeud)

    def obtenir_dernier_noeud(self):
        # Retourne le dernier noeud ajouté (pour l'exploration en profondeur)
        return self.noeuds[-1] if self.noeuds else None

    def contient_noeud(self, noeud):
        # Vérifie si un noeud est déjà dans la liste
        return noeud in self.noeuds
