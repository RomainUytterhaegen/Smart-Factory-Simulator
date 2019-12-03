from Obstacle import Obstacle
from Tache import Tache
from random import *


class Atelier(Obstacle):
    def __init__(self, pos1: tuple, pos2: tuple, utilite: str, taches: Tache):
        Obstacle.__init__(self, pos1, pos2)
        self.utilite = utilite
        self.taches = taches
        self.temps_avant_tache = random.randint(30,300)

    def get_utilite(self):
        """
        Retourne l'utilité de l'atelier
        """
        return self.utilite
