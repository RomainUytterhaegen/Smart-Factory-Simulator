class Ouvrier():
    def __init__(self,id,posInit,radius):
        self.id = id            #int
        self.posInit = posInit  #tuple (x,y), position initiale (fixe)
        self.pos = posInit      #tuple (x,y), position en temps réel, amenée à changer
        self.radius = radius    #int, rayon correspondant à la limite de déplacement de l'ouvrier
        self.vitMarche = 1

    def getPosInit(self):
        """
        Retourne la position initiale de l'ouvrier (tuple)
        :return:
        """
        return self.posInit

    def getPos(self):
        """
        Retourne la position actuelle de l'ouvrier (tuple)
        :return:
        """
        return self.pos

    def getRadius(self):
        """
        Retourne le rayon de déplacement de l'ouvrier (int)
        :return:
        """
        return self.radius

    def in_radius(self, pos):
        """
        Retourne true si la position passée en paramètre est dans le rayon de déplacement de l'ouvrier, false sinon
        :param pos:
        :return:
        """
        return ((self.getPosInit()[0] - self.getRadius() <= self.getPos[0] + pos[0] <= self.getPosInit()[0] + self.getRadius())\
               and self.getPosInit()[1] - self.getRadius() <= self.getPos[1] + pos[1] <= self.getPosInit()[1] + self.getRadius())



    def seDeplacer(self,tup):
        """
        Déplace l'ouvrier à la position passée en paramètre
        """
        self.pos = tup




if __name__ == "__main__":
    ouvr1 = Ouvrier(2,(10,7),5)






