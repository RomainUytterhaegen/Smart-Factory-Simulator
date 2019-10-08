class Ouvrier():
    def __init__(self,id,posInit,radius,vitMarche):
        self.id = id            #int
        self.posInit = posInit  #tuple (xInit,yInit), position initiale,fixe et mémorisée
        self.pos = posInit      #tuple (x,y), position en temps réel, amenée à changer
        self.radius = radius    #int, rayon correspondant à la limite de déplacement de l'ouvrier


        self.vitMarche = vitMarche

    def getPos(self):
        """
        Retourn la position de l'ouvrier
        :return:
        """
        return self.Pos
    def getVitMarche(self):
        """
        Retourne la vitesse de marche de l'ouvrier
        :return:
        """
        return self.vitMarche
    def genereDestination(self):
        """
        Génère aléatoirement une destination pour l'ouvrier.
        Celle ci ne peut se trouver au delà du radius
        Retourne les coordonnées de sa destination
        :return:
        """
        pass
    def allerA(self,x,y):
        """
        Permet à l'ouvrier de se déplacer d'un endroit à un autre,
        Modifie sa position pos mais pas posInit
        :return:
        """
        pass
