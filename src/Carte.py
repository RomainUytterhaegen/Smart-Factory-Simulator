from Borne import Borne
from Atelier import Atelier
from Ouvrier import Ouvrier
from Obstacle import Obstacle
from Robot import Robot
from Ouvrier import Ouvrier
from random import choice


class Carte:

    def __init__(self, nom:str, x:int, y:int,
                 listeObstacle:list=None, listeRobot:list=None, listeOuvrier:list=None):
        """
        Crée un tableau de dimension x par y.
        Pour chaque Obstacle, le mettre dans le tableau (0 pour un espace vide, 1 pour un obstacle, 2 pour un atelier, 3 pour une borne).
        """
        if not listeObstacle:
            listeObstacle = []
        if not listeRobot:
            listeRobot = []
        if not listeOuvrier:
            listeOuvrier = []

        self.listeBorne = []
        self.listeAtelier = []
        self.listeRobot = listeRobot
        self.nom = nom
        self.listeObstacle = listeObstacle
        self.listeOuvrier= listeOuvrier
        self.listeTache = []
        
        self.x = x
        self.y = y

        for i in range(0,len(self.listeObstacle)):
            self.ajouterObstacle(listeObstacle[i])

    def getObstacles(self):
        """
        Retourne tout les obstacles
        """
        return self.listeObstacle

    def getPosObstacles(self):
        """
        Retourne l'ensemble des cases prises par les Obstacles.
        """
        res = []
        for obstacle in self.listeObstacle:
            for i in range(obstacle.getPos1()[1],obstacle.getPos2()[1]):
                for j in range(obstacle.getPos1()[0],obstacle.getPos2()[0]):
                    res.append((i,j))
        return res

    def ajouterObstacle(self,obstacle:Obstacle):
        """
        Méthode qui ajoute un obstacle à la Carte.
        """
        #GERER LE CAS OU 2 OBSTACLES SONT SUPERPOSES

    def supprimerObstacle(self,idObstacle:int):
        """
        Méthode qui supprime un obstacle de la Carte.
        """
        res = -1
        i = 1
        #ON CHERCHE L'OBSTACLE DANS LA CARTE
        while i<len(self.listeObstacle) and res != idObstacle:
            if self.listeObstacle[i].getId() == idObstacle:
                res = i
            i+=1
        if i != -1:
            #ON SUPPRIME L'OBSTACLE DE LA CARTE
            self.listeObstacle.pop(res)
        else:
            #CAS OÙ L'OBSTACLE N'EST PAS DANS LA CARTE
            raise EnvironmentError("Il n'y a pas cet objet sur la carte.")

    def getRobots(self):
        """
        Retourne la liste de tout les robots sur la carte
        """
        return self.listeRobot

    def getPosRobots(self):
        """
        Retourne l'ensemble des cases prises par les robots
        """
        res = []
        for robot in self.listeRobot:
            res.append(robot.pos)
        return res

    def ajouterRobot(self,robot:Robot):
        """
        Ajoute un robot à la carte.
        """
        #GERER LE CAS OÙ LE ROBOT NE PEUT ÊTRE POSÉ

    def supprimerRobot(self,idRobot:int):
        """
        Supprime un robot de l'environnement
        """
        res = -1
        i = 1
        #ON CHERCHE LE ROBOT DANS LA CARTE
        while i<len(self.listeRobot) and res != idRobot:
            if self.listeRobot[i].getId() == idRobot:
                res = i
            i+=1
        if i != -1:
            #ON SUPPRIME LE ROBOT DE LA CARTE
            self.listeRobot.pop(res)
        else:
            #CAS OÙ LE ROBOT N'EST PAS DANS LA CARTE
            raise EnvironmentError("Il n'y a pas cet objet sur la carte.")

    def getAteliers(self):
        """
        Retourne la liste des ateliers
        """
        return self.listeAtelier

    def getPosAteliers(self):
        """
        Retourne l'ensemble des positions prises par les ateliers
        """
        res = []
        for atelier in self.listeAtelier:
            for i in range(atelier.getPos1()[1],atelier.getPos2()[1]):
                for j in range(atelier.getPos1()[0],atelier.getPos2()[0]):
                    res.append((i,j))
        return res

    def ajouterAtelier(self,atelier:Atelier):
        """
        Ajoute un atelier à la Carte
        """
        #GERER LE CAS OÙ L'ATELIER NE PEUT PAS ÊTRE POSÉ

    def supprimerAtelier(self,idAtelier:int):
        """
        Supprime un robot de l'environnement
        """
        res = -1
        i = 1
        #ON CHERCHE L'OBSTACLE DANS LA CARTE
        while i<len(self.listeAtelier) and res != idAtelier:
            if self.listeAtelier[i].getId() == idAtelier:
                res = i
            i+=1
        if i != -1:
            #ON SUPPRIME L'OBSTACLE DE LA CARTE
            self.listeAtelier.pop(res)
        else:
            #CAS OÙ L'OBSTACLE N'EST PAS DANS LA CARTE
            raise EnvironmentError("Il n'y a pas cet objet sur la carte.")
    
    def getBornes(self):
        """
        retourne les Bornes de la Carte
        """
        return self.listeBorne

    def getPosBornes(self):
        """
        Retourne l'ensemble des positions prises par les bornes.
        """
        res = []
        for borne in self.listeBorne:
            res.append(borne.getPos1())
        return res

    def ajouterBorne(self,borne:Borne):
        """
        Ajoute une Borne dans la Carte
        """
        #GERER SI ON PEUT POSER LA BORNE 
        pass

    def supprimerBorne(self,idBorne:int):
        """
        Supprime une Borne de la Carte
        """
        res = -1
        i = 1
        #ON CHERCHE LA BORNE DANS LA CARTE
        while i<len(self.listeBorne) and res != idBorne:
            if self.listeBorne[i].getId() == idBorne:
                res = i
            i+=1
        if i != -1:
            #ON SUPPRIME LA BORNE DE LA CARTE
            self.listeBorne.pop(res)
        else:
            #CAS OÙ LA BORNE N'EST PAS DANS LA CARTE
            raise EnvironmentError("Il n'y a pas cet objet sur la carte.")

    def getPosImpossible(self):
        """
        Retourne l'ensemble des cases de l'usines non traversables
        """
        return self.getPosAteliers() + self.getPosObstacles() + self.getPosRobots() + self.getPosBornes()

    def tour_simulation(self):
        """
        Réalise un tour de simulation
        :return: True si les robots n'ont tous plus rien à faire
        """
        nb_afk = 0

        for robot in self.listeRobot:
            if robot == -1:
                nb_afk += robot.choixTache()
            else:
                robot.faireTache()

        return nb_afk == len(self.listeRobot)


    def deplacerRobot(self,robot:Robot,):
        pass

    def get_voisins(self, pos):
        """
        Retourne la liste des cases voisines d'une case
        :param pos:
        :return:
        """
        x, y = pos
        return [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]

    def case_occupee(self, pos):
        return pos in self.getObstacles()

    def deplaceOuvrier(self,ouv:Ouvrier):
        """
        Déplace l'ouvrier d'une case disponible, à sa portée et dans son rayon de déplacement
        :param ouv: Ouvrier que l'on souhaite déplacer
        """
        ouv.seDeplacer(choice(filter(self.case_occupee, list(filter(ouv.in_radius, self.get_voisins(ouv.getPos()))))))





        

