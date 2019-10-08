from Obstacle import *
class Borne(Obstacle):
    def __init__(self, id, pos1, pos2, type, vitCharge):
        Obstacle.__init__(self, id, pos1, pos2, type)
        self.vitCharge = vitCharge

    def getviteCharge(self):
        """
        Retourne la vitesse de charge de la borne
        :return:
        """
        return self.viteCharge