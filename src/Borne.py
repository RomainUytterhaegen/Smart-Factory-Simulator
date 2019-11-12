import time
from Obstacle import Obstacle
from Robot import Robot


class Borne(Obstacle):

    tauxRecharge = 1

    def __init__(self,id:int,pos1:tuple,pos2:tuple):
        Obstacle.__init__(self, id, pos1, pos1)
        self.used = False

    def recharge(self,robot:Robot):
        """
        Recharge le robot jusqu'à ce que sa batterie soit pleine
        :param:
        :return:
        """
        while not(robot.isFull()):
            self.used = True
            robot.remplirBatterie(Borne.tauxRecharge)
        self.used = False

    def valideCharge(self, robot:Robot):
        """
        Méthode vérifiant que la borne est disponible et que la batterie du robot
        n'est pas déjà remplie
        Retourne True si elle peut charger le robot,false sinon
        :return:
        """
        b = False
        if self.used == False:
            if robot.isFull():
                raise EnvironmentError('Le robot est déjà rechargé')
            else:
                b = True
        return b


        
if __name__ == "__main__":
    born1 = Borne(1,(4,3),(5,6))
    print("ID : ", born1.getId())
    print("Pos 1 :", born1.getPos1())
    print("Pos 2 : ", born1.getPos2())
    print("Hauteur : ", born1.getHeight())
    print("Largeur : ", born1.getWidth())
    rob = Robot(2,False,True,(5,7),2)
    born1.recharge(rob)
