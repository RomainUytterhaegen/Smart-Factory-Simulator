from Obstacle import *
class Atelier(Obstacle):
    def __init__(self,id,pos1,pos2,type,utilite):
        Obstacle.__init__(self,id,pos1,pos2,type)
        self.utilite = utilite

    def getUtilite(self):
        """
        Retourne l'utilité de l'atelier
        :return:
        """
        return self.utilite