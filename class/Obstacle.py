
class Obstacle:
    def __init__(self, id,  pos1, pos2,  type ):
        self.id = id
        self.pos1 = pos1
        self.pos2 = pos2
        self.type = type

    def getType(self):
        """
        Retourne le type de l'obstacle
        :return:
        """
        return self.type

    def getPos1(self):
        """
        Retourne les coordonnées du coin bas_gauche de l'obstacle
        :return:
        """
        return self.pos1

    def getPos2(self):
        """
        Retourne les coordonnées du coin haut_droit de l'obstacle
        :return:
        """
        return self.pos2

    def getLength(self):
        """
        Retourne la longueur de l'obstacle (axe Y)
        :return:
        """
        return pos2[1]-pos1[1]

    def getWidth(self):
        """
        Retourne la largeur de l'obstacle (axe X)
        :return:
        """
        return pos2[0]-pos1[0]

if __name__ == "__main__":
    Obst1 = Obstacle(1, )