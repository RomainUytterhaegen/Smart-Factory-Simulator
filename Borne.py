import time

class Borne(Obstacle):
    tauxRecharge = 10

    def __init__(self):
        self.used = False

    def recharge(self, robot):
        if robot.isFull():
            raise EnvironmentError('Le robot est déjà rechargé')
        while not(robot.isFull()):
            self.used = True
            time.sleep(2) # simule le temps pour recharger
            robot.remplirBatterie(Borne.tauxRecharge)
        self.used = False
        return None        

        