import random


class Tache:

    def __init__(self, **kwargs):
        """
        Les arguments passent en kwargs pour éviter de faire des héritages pour 2 attributs
        :param kwargs: "valid", "pos_fin", "pos_depart"
        """
        if "valide" in kwargs:
            self.valide = kwargs["valide"]  # Si la tâche est utilisable ou non (initialisation du robot)
        else:
            self.valide = False

        if "pos_fin" in kwargs:
            self.fin = kwargs["pos_fin"]
            self.type = "Transport"
        else:
            self.fin = (0, 0)
            self.type = "Assemblage"

        if "pos_depart" in kwargs:
            self.depart = kwargs["pos_depart"]  # Si la tâche est utilisable ou non (initialisation du robot)
        else:
            self.depart = (0, 0)


        self.points = random.randint(1, 1000)  # à changer plus tard, la c'est juste pour test
        self.duree = random.randint(50, 200)  # Durée en secondes
        self.enchere = False
        self.Tfin = 0
        # on dit qu'une tâche a 10% de chance d'être une enchère
        if random.randint(0,100) <= 10:
            self.enchere = True

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
        return self.valide

    def __str__(self):
        return f"Points : {self.points} , durée : {self.duree} secondes , type : {self.type}"
