from Tache import Tache

class TacheTransport(Tache) :

    def __init__(self,points=0, duree=0,enchere = False):
        Tache.__init__(points=self.points,duree=self.duree,enchere=self.enchere)