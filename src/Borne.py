# import time
from Obstacle import Obstacle
from Robot import Robot
from sys import stderr


class Borne(Obstacle):

    TAUX_RECHARGE = 100

    def __init__(self, id_borne: int, pos1: tuple):
        Obstacle.__init__(self, id_borne, pos1, pos1)
        self.used = False

    def recharge(self, robot: Robot):
        """
        Recharge le robot jusqu'à ce que sa batterie soit pleine
        :param:
        :return:
        """
        if not robot.is_full():
            self.used = True
            robot.remplir_batterie(Borne.TAUX_RECHARGE)
        else:
            print('Le robot est chargé', file=stderr)
            self.used = False