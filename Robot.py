class Robot:

    def __init__(self,idRobot,transport,assemblage,pos,vitesse = 2):
        self.id = idRobot # int
        self.transport = transport #booléen
        self.assemblage = assemblage #booléen
        self.vitesse = vitesse #int
        self.batterie = 1000 # chaque case parcourue, 1 de batterie en moins
        self.pos = pos # ((x1,y1),(x2,y2))
    
    def peutFaire(self,tache):
        """
        Définit si le robot peut faire la tâche (s'il a assez d'autonomie pour aller à l'équipement, faire la tâche puis aller se recharger.)
        """

    def allerBorne(self,borne):
        """
        Détermine le chemin à prendre pour aller à une borne donnée.
        """

    def distance(self,obstacle):
        """ 
        Retourne le nombre de cases à parcourir pour aller à un équipement
        ou une borne. Attention, juste le nombre , pas le chemin à parcourir.
        """


    def autonomie(self):
        """
        Retourne la distance que peut faire le robot avant de tomber en panne
        """
        return self.batterie
    
    def competences(self):
        """
        Retourne les compétences du robot sous forme d'un tableau booléen
        suivant : [transport,assemblage]
        """
        return [self.transport,self.assemblage]

    def vitesse(self):
        """
        Retourne la vitesse du robot
        """
        return self.vitesse

    def allerA(self,x,y):
        """
        Fait avancer le robot sur une case donnée. Attention, vérifier que c'est une case autour du Robot, si ce n'est pas un obstacle.
        Enlève de l'autonomie à la batterie du robot.
        """