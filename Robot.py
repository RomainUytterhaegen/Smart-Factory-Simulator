from Tache import Tache

class Robot:

    def __init__(self,idRobot:int,transport:bool,assemblage:bool,pos:tuple,vitesse = 2):
        self.id = idRobot # int
        self.transport = transport #booléen
        self.assemblage = assemblage #booléen
        self.vitesse = vitesse #int
        self.batterie = 1000 # chaque case parcourue, 1 de batterie en moins
        self.pos = pos # (x2,y2)
        self.points = 0
    
    def choixTache(self):
        """
        Le robot cherche dans la base de donnée une tâche qu'il peut faire avec ses compétences. Si c'est une tâche simple, premier arrivée , premier servi.
        (Pour le moment on s'occupe pas d'enchère , on voit après). Retourne une tâche, si aucune tâche n'est disponible/accessible, retourne False.
        """
        pass

    def faireTache(self,tache:Tache):
        """
        Effectue la tâche en paramètre. Récupère le temps requis pour faire un assemblage, ou le temps pour le transporter. Simule cette période.
        Retourne True si la tâche a été effectuée dans les temps, False sinon.
        """
        pass

    def allerBorne(self):
        """
        Trouve une borne qui n'est pas occupée, détermine le Chemin pour y aller, puis s'y dirige. 
        """
        pass

    def getDistance(self,obstacle):
        """ 
        Retourne le nombre de cases à parcourir pour aller à un équipement
        ou une borne. Attention, juste le nombre , pas le chemin à parcourir.
        Instancie un Chemin puis retounne le nombre de cases à parcourir
        """
        pass


    def getAutonomie(self):
        """
        Retourne la distance que peut faire le robot avant de tomber en panne
        """
        return self.batterie
    
    def getCompetences(self):
        """
        Retourne les compétences du robot sous forme d'un tableau booléen
        suivant : [transport,assemblage]
        """
        return [self.transport,self.assemblage]

    def getVitesse(self):
        """
        Retourne la vitesse du robot
        """
        return self.vitesse

    def allerA(self,x,y):
        """
        Fait avancer le robot sur une case donnée. Attention, vérifier que c'est une case autour du Robot, si ce n'est pas un obstacle.
        Enlève de l'autonomie à la batterie du robot.
        """
        if x <= self.pos[0]+1 and x >= self.pos[0]-1 and y <= self.pos[1]+1 and y >= self.pos[1]-1:
            self.pos = (x,y)
            self.batterie-=1 
    
    def encherir(self,tache):
        """
        Le robot estime son prix minimal pour être payé(en fonction de sa distance, ses compétences, vitesse , ect), il propose un prix en fonction de ce calcul.
        """
        pass