import random

class Tache :

    def __init__(self, enchere):
        self.points = random.randint(1, 1000) #Surement à changer plus tard, la c'est juste pour test
        self.duree = random.randint(1, 180)
        if enchere == True:
            self.enchere = random.randint(0, 501)
        else:
            self.enchere = 0

    def getPoints(self):
        pts = self.points
        return pts

    def getDuree(self):
        res = self.duree
        return res

    def getEnchere(self):
        res = self.enchere
        return res

    def __str__(self):
        return "Points : {0} , durée : {1} minutes".format(self.points, self.duree)

if __name__ == "__main__":
    tache1 = Tache(False)
    print("\n")
    print(tache1)
    print(tache1.getDuree())
    print(tache1.getPoints())
    print(tache1.getEnchere())