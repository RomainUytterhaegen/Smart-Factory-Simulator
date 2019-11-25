# import time
from Obstacle import Obstacle
from Robot import Robot


class Borne(Obstacle):

    TAUX_RECHARGE = 1

    def __init__(self, id_borne: int, pos1: tuple):  # , pos2: tuple):
        Obstacle.__init__(self, id_borne, pos1, pos1)
        self.used = False

    def recharge(self, robot: Robot):
        """
        Recharge le robot jusqu'à ce que sa batterie soit pleine
        :param:
        :return:
        """
        while not(robot.is_full()):
            self.used = True
            robot.remplir_batterie(Borne.TAUX_RECHARGE)
        self.used = False

    def valide_charge(self, robot: Robot):
        """
        Méthode vérifiant que la borne est disponible et que la batterie du robot
        n'est pas déjà remplie
        Retourne True si elle peut charger le robot,false sinon
        :return:
        """
        b = False
        if not self.used:
            if robot.is_full():
                raise EnvironmentError('Le robot est déjà rechargé')
            else:
                b = True
        return b
