import random


class Tache:

    def __init__(self, **kwargs):
        """
        Les arguments passent en kwargs pour éviter de faire des héritages pour 2 attributs
        :param kwargs: "valid", "pos_fin", "pos_depart"
        """

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
            self.valide = False  # Si la tâche est utilisable ou non (initialisation du robot)

        self.points = random.randint(1, 1000)  # à changer plus tard, la c'est juste pour test
        self.duree = random.randint(50, 200)  # Durée en secondes
        self.enchere = False
        self.t_actuel = 0
        # on dit qu'une tâche a 10% de chance d'être une enchère
        if random.randint(0, 100) <= 10:
            self.enchere = True

    def get_points(self):
        return self.points

    def get_duree(self):
        return self.duree

    def get_enchere(self):
        return self.enchere
    
    def get_type(self):
        return self.type

    def liste_enchere(self):
        pass

    def get_t_actuel(self):
        return self.t_actuel

    def attribuer_points(self):
        """
        Donne le nombre de points si la tâche a été faite dans les délais, donne le montant de l'amende sinon.
        """
        if self.t_actuel > self.duree:
            res = (self.t_actuel-self.duree) * 3
        else:
            res = self.points
        return res

    def __bool__(self):
        return self.valide

    def __str__(self):
        return f"Points : {self.points} , durée : {self.duree} secondes , type : {self.type}"
