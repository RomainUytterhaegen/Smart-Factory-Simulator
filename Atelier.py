from Obstacle import Obstacle

class Atelier(Obstacle):
    def __init__(self,id,pos1,pos2,utilite,taches):
        Obstacle.__init__(self,id,pos1,pos2)
        self.utilite = utilite
        self.taches = taches

    def getUtilite(self):
        """
        Retourne l'utilité de l'atelier
        """
        return self.utilite

if __name__ == "__main__":
    atel1 = Atelier(1,(5,6),(6,6),"Assemblage visses boulons",[])
    print("ID : ", atel1.getId())
    print("Pos 1 :", atel1.getPos1())
    print("Pos 2 : ", atel1.getPos2())
    print("Hauteur : ", atel1.getHeight())
    print("Largeur : ", atel1.getWidth())
    print("Utilité : ", atel1.getUtilite())