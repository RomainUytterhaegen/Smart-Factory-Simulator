from Obstacle import Obstacle

class Atelier(Obstacle):
    def __init__(self,id:int,pos1:tuple,pos2:tuple,utilite):
        Obstacle.__init__(self, idObstacle:int,  pos1:tuple, pos2:tuple)
        self.utilite = utilite

    def getUtilite(self):
        """
        Retourne l'utilité de l'atelier (assemblage, transport)
        :return:
        """
        return self.utilite