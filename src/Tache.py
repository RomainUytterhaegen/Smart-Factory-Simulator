import random
from Robot import Robot

class Tache:

    def __init__(self):
        self.points = random.randint(1, 1000) #Surement à changer plus tard, la c'est juste pour test
        self.duree = random.randint(50, 200) # Durée en secondes
        self.enchere = False

        #on dit qu'une tâche a 10% de chance d'être une enchère
        if random.randint(0,100) <=10:
            self.enchere = True

        if random.randint(0,100) <= 50:
            self.type= "Assemblage"
        else:
            self.type = "Transport"

    def getPoints(self):
        return self.points

    def getDuree(self):
        return self.duree

    def getEnchere(self):
        return self.enchere
    
    def getType(self):
        return self.type


    def __str__(self):
        return "Points : {0} , durée : {1} secondes".format(self.points, self.duree)

    def listeEnchere(self):
        pass
