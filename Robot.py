class Robot:

    def __init__(self,idRobot,transport,assemblage,vitesse = 2):
        self.id = idRobot
        self.transport = transport
        self.assemblage = assemblage
        self.vitesse = vitesse
        self.batterie = 1000 # chaque case parcourue, 1 de batterie en moins
    
    def peutFaire(self,tache):
        #Faut récupérer la distance entre le robot et l'endroit où faire la tâche, l'ajouter à la distance entre la tâche et la borne de recharge et estimer
        #l'autonomie pour s'assurer que le robot ne tombe pas en panne.

    def allerBorne(self,borne):
        #détermine le chemin à prendre pour aller à une borne donnée.

    def distance(self,obstacle):
        # retourne le nombre de cases parcourues pour aller à un équipement
        # ou une borne


    def autonomie(self):
        #retourne la distance que peut faire le robot avant de tomber en panne
        return self.batterie
    
    def competences(self):
        # retourne les compétences du robot sous forme d'un tableau booléen
        # suivant : [transport,assemblage]
        return [self.transport,self.assemblage]

    def vitesse(self):
        #retourne la vitesse du robot
        return self.vitesse
    


