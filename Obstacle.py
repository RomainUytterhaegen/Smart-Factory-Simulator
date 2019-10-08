
class Obstacle:
    def __init__(self, idObstacle:int,  pos1:tuple, pos2:tuple):
        self.id = idObstacle
        self.pos1 = pos1
        self.pos2 = pos2


    def getPos1(self):
        """
        Retourne les coordonnées du coin bas_gauche de l'obstacle
        :return: Tuple
        """
        return self.pos1

    def getPos2(self):
        """
        Retourne les coordonnées du coin haut_droit de l'obstacle
        :return: Tuple
        """
        return self.pos2

    def getHeight(self):
        """
        Retourne la hauteur de l'obstacle (axe Y)
        :return:
        """
        return self.pos2[1]-self.pos1[1]

    def getWidth(self):
        """
        Retourne la largeur de l'obstacle (axe X)
        :return:
        """
        return self.pos2[0]-self.pos1[0]
