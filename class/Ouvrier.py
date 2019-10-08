from Obstacle import *
class Ouvrier(Obstacle):
    def __init__(self,id,pos1,pos2,type,utilite):
        Obstacle.__init__(self,id,pos1,pos2,type)
        self.vitMarche = vitMarche

    def getVitMarche(self):
        """
        Retourne la vitesse de marche de l'ouvrier
        :return:
        """
        return self.vitMarche