import random

class Tache :

    def __init__(self):
        self.points = random.randint(1, 1000) #Surement à changer plus tard, la c'est juste pour test
        self.duree = random.randint(50, 200) # Durée en secondes
        self.enchere = False
        #on dit qu'une tâche a 10% de chance d'être une enchère
        chance = random.randint(0,100)
        if chance <=10:
            self.enchere = True

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
        return "Points : {0} , durée : {1} secondes".format(self.points, self.duree)


#TEST
if __name__ == "__main__":
    tache1 = Tache()
    print("\n")
    print(tache1)
    print(tache1.getDuree())
    print(tache1.getPoints())
    print(tache1.getEnchere())