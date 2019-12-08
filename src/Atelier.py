from Obstacle import Obstacle
from Tache import Tache


class Atelier(Obstacle):
    def __init__(self, id_atelier: int, pos1: tuple, pos2: tuple, taches: Tache):
        Obstacle.__init__(self, id_atelier, pos1, pos2)
        self.taches = taches
        self.liste_gen_taches = []

    def gen_tache(self, tache: Tache, temps: int):
        """
        Ajoute une tache a la liste des taches générée par cet atelier
        :param tache: La tache générée
        :param temps: Le temps entre chaque génération
        """
        self.liste_gen_taches.append((tache, temps, temps))  # le premier temps est celui de référence

    def update_taches(self):
        retour_taches = []
        for t in range(len(self.liste_gen_taches)):
            self.liste_gen_taches[t][-1] -= 1
            if self.liste_gen_taches[t][-1] <= 0:
                self.liste_gen_taches[t][-1] = self.liste_gen_taches[t][1]
                retour_taches.append(self.liste_gen_taches[t][0])
        return retour_taches
