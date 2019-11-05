from Tache import Tache
from Carte import Carte
from Obstacle import Obstacle
from Chemin import Chemin


class Robot:

    def __init__(self,idRobot:int,transport:bool,assemblage:bool,pos:tuple,vitesse = 2):
        self.idRobot = idRobot # int
        self.transport = transport #booléen
        self.assemblage = assemblage #booléen
        self.vitesse = vitesse #float
        self.batterie = 1000 # chaque case parcourue, 1 de batterie en moins
        self.pos = pos # (x2,y2)
        self.points = 0
    
    def choixTache(self,carte:Carte):
        """
        Le robot cherche dans la base de donnée une tâche qu'il peut faire avec ses compétences. Si c'est une tâche simple, premier arrivée , premier servi.
        (Pour le moment on s'occupe pas d'enchère , on voit après). Retourne une tâche, si aucune tâche n'est disponible/accessible, retourne False.
        TODO méthode allerA()
        """
        
        #Récupère les tâches faisables par le robot.(compétence et autonomie) S'il peut en faire une , il la choisit. Retourne false si aucune tache n'est disponible

        #Détermine le chemin pour aller 
        pass



    #def faireTache(self,tache:Tache):
    #    """
    #    Va à l'endroit de la tâche.
    #
    #    Effectue la tâche en paramètre. Récupère le temps requis pour faire un assemblage, ou le temps pour le transporter. Simule cette période.
    #    Retourne True si la tâche a été effectuée dans les temps, False sinon. (Peut être instancier un objet chronomètre ?)
    #    TODO ALgorithme pour trouver son chemin parmi les obstacles
    #    """
    #    pass

    def allerBorne(self, carte:Carte):
        """
        Trouve une borne qui n'est pas occupée, détermine le Chemin pour y aller, puis s'y dirige. 
        """
        
        # Récupère l'ensemble des bornes non occupées

        #Se dirige à la borne 

        #Se recharge
        pass

    def getId(self):
        """
        Retourne l'indice du Robot
        """
        return self.idRobot

    def getDistance(self,obstacle):
        """ 
        Retourne le nombre de cases à parcourir pour aller à un équipement
        ou une borne. Attention, juste le nombre , pas le chemin à parcourir.
        Instancie un Chemin puis retounne le nombre de cases à parcourir
        """
        
        # Etablit un chemin , compte le nombre d'étapes
        pass


    def getAutonomie(self,carte:Carte):
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

    def allerA(self,obstacle:Obstacle,carte:Carte):
        """
        Déplace le robot jusqu'à un point donné. Vérifie qu'il avance une case par une(voir code ci-dessous)
        TODO algorithme pour trouver son chemin parmi les obstacles 
        """
                

        #Instancie un chemin

        #Déplace le robot une case par une jusqu'à destination
        pass
    
    def pourCombien(self,tache:Tache):
        """
        Le robot estime son prix minimal pour être payé(en fonction de sa distance, ses compétences, vitesse , ect), il propose un prix en fonction de ce calcul.
        le reste sera géré par la classe TacheEnchere.
        """
        return self.getDistance(tache)*self.vitesse + tache.duree()

    def isFull(self):
        """
        Retourne TRUE si la batterie du Robot est chargée , false sinon
        """
        return self.batterie == 1000

    def remplirBatterie(self,recharge:float):
        """
        Recharge la batterie d'une certaine quantité
        """
        self.batterie+=recharge

