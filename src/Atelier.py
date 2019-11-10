from Obstacle import Obstacle

class Atelier(Obstacle):
    def __init__(self,id,pos1,pos2,utilite,taches):
        Obstacle.__init__(self,id,pos1,pos2)
        self.utilite = utilite
        self.taches = taches

    def getUtilite(self):
        """
        Retourne l'utilité de l'atelier
        """
        return self.utilite
