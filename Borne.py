import time

class Borne(Obstacle):
    tauxRecharge = 10

    def __init__(self):
        self.used = False

    def recharge(self, robot):
        if robot.isFull():
            raise EnvironmentError('Le robot est déjà rechargé')
        while not(robot.isFull()):
            time.sleep(2)
            robot.remplirBatterie(Borne.tauxRecharge)
        return None        

        