from Obstacle import *
class Ouvrier():
    def __init__(self,id,pos,vitMarche):
        self.id = id
        self.pos = pos
        self.vitMarche = vitMarche

    def getPos(self):
        """
        Retourn la position de l'ouvrier
        :return:
        """
        return self.Pos
    def getVitMarche(self):
        """
        Retourne la vitesse de marche de l'ouvrier
        :return:
        """
        return self.vitMarche