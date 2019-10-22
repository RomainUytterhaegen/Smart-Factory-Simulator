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
            #On update la base de donnée pour dire que la borne est occupée
            while not(robot.isFull()):
                self.used = True
                #time.sleep(1) # simule le temps pour recharger
                robot.remplirBatterie(Borne.tauxRecharge)
            self.used = False
            #On update la base de donnée pour dire que la borne est libre
        
if __name__ == "__main__":
    born1 = Borne(1,(4,3),(5,6))
    print("ID : ", born1.getId())
    print("Pos 1 :", born1.getPos1())
    print("Pos 2 : ", born1.getPos2())
    print("Hauteur : ", born1.getHeight())
    print("Largeur : ", born1.getWidth())
    rob = Robot(2,False,True,(5,7),2)
    born1.recharge(rob)
