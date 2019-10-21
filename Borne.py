import time
from Obstacle import Obstacle
from Robot import Robot


class Borne(Obstacle):

    tauxRecharge = 10

    def __init__(self,id:int,pos1:tuple,pos2:tuple):
        Obstacle.__init__(self, id, pos1, pos2)
        self.used = False

    def recharge(self, robot:Robot):
        if robot.isFull():
            raise EnvironmentError('Le robot est déjà rechargé')
        if self.used == False:
            while not(robot.isFull()):
                self.used = True
                #time.sleep(1) # simule le temps pour recharger
                robot.remplirBatterie(Borne.tauxRecharge)
            self.used = False
