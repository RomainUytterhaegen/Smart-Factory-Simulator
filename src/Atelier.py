from Obstacle import Obstacle
from Tache import Tache


class Atelier(Obstacle):
    def __init__(self, pos1: tuple, pos2: tuple, utilite: str, taches: Tache):
        Obstacle.__init__(self, pos1, pos2)
        self.utilite = utilite
        self.taches = taches

    def get_utilite(self):
        """
        Retourne l'utilité de l'atelier
        """
        return self.utilite
