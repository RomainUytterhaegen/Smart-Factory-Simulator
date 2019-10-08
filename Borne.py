import time
from Obstacle import Obstacle

class Borne(Obstacle):
    Obstacle.__init__(self, idObstacle:int,  pos1:tuple, pos2:tuple)
    tauxRecharge = 10

    def __init__(self,id,pos1,pos2):
        Obstacle.__init__(self, id, pos1, pos2)
        self.used = False

    def recharge(self, robot):
        if robot.isFull():
            raise EnvironmentError('Le robot est déjà rechargé')
        while not(robot.isFull()):
            self.used = True
            time.sleep(2) # simule le temps pour recharger
            robot.remplirBatterie(Borne.tauxRecharge)
        self.used = False
        