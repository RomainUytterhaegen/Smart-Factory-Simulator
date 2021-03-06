import random


class Tache:

    ASSEMBLAGE = 1
    TRANSPORT = 2

    def __init__(self, **kwargs):
        """
        Les arguments passent en kwargs pour éviter de faire des héritages pour 2 attributs
        :param kwargs: "pos_fin", "pos_depart"
        """
        self.valide = True

        if "pos_fin" in kwargs:
            self.fin = kwargs["pos_fin"]
            self.type = Tache.TRANSPORT
        else:
            self.fin = (-1, -1)
            self.type = Tache.ASSEMBLAGE
            self.temps_assemblage = random.randint(15,20)

        if "liste_depart" in kwargs:
            self.liste_depart = kwargs["liste_depart"]
        elif "pos_depart" in kwargs:
            self.depart = kwargs["pos_depart"]  # Si la tâche est utilisable ou non (initialisation du robot)
        else:
            self.depart = (0, 0)
            self.valide = False  # Si la tâche est utilisable ou non (initialisation du robot)

        self.points = random.randint(1, 1000)  # à changer plus tard, la c'est juste pour test
        self.duree = random.randint(50, 200)  # Durée en tour
        self.enchere = False
        self.commence = False
        # on dit qu'une tâche a 10% de chance d'être une enchère
        if random.randint(0, 100) <= 10:
            self.enchere = True


    def attribuer_points(self):
        """
        Donne le nombre de points si la tâche a été faite dans les délais, donne le montant de l'amende sinon.
        """
        if self.duree < 0:
            res = self.duree * 3
        else:
            res = self.points
        return res

    def __bool__(self):
        return self.valide

    def __str__(self):
        return f"Points : {self.points} , durée : {self.duree} secondes , type : {self.type}"
