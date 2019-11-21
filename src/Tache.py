import random


class Tache:

    def __init__(self, pos_depart:tuple, valid:bool = True ):
        self.valid = valid  # Si la tâche est utilisable ou non (initialisation du robot)
        self.points = random.randint(1, 1000)  # à changer plus tard, la c'est juste pour test
        self.duree = random.randint(50, 200)  # Durée en secondes
        self.enchere = False
        self.Tfin = 0
        self.depart = pos_depart
        # on dit qu'une tâche a 10% de chance d'être une enchère
        if random.randint(0,100) <= 10:
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

    def listeEnchere(self):
        pass

    def getTfin(self):
        return self.Tfin

    def setTfin(self, tdebut: int):
        self.Tfin = tdebut + self.duree

    def getAmende(self):
        Tfin = self.getTfin()
        Tdebut = 0
        amende = 0
        while Tdebut <= Tfin:
            Tdebut += 1
            if Tdebut == Tfin:
                amende = self.points / 2
        return amende

    def __bool__(self):
        return self.valid

    def __str__(self):
        return f"Points : {self.points} , durée : {self.duree} secondes , type : {self.type}"
