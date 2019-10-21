class Ouvrier():
    def __init__(self,id,pos,radius,vitMarche):
        self.id = id            #int
        self.pos = pos          #tuple (x,y), position en temps réel, amenée à changer
        self.radius = radius    #int, rayon correspondant à la limite de déplacement de l'ouvrier
        self.vitMarche = vitMarche = 1

    def seDeplacer(self):
        """
        A chaque appel de cette méthode , l'ouvrir se déplace d'une case, tout en restant dans sa zone de déplacement
        """
        pass