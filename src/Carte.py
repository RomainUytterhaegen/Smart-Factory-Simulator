from Borne import Borne
from Atelier import Atelier
from Ouvrier import Ouvrier
from Obstacle import Obstacle
from Robot import Robot
from Ouvrier import Ouvrier
from random import choice
from Chemin import Chemin, heuristic
from sys import stderr

class Carte:

    def __init__(self, nom: str, x: int, y: int,
                 listeObstacle: list=None, liste_robot: list=None, listeOuvrier: list=None):
        """
        Crée un tableau de dimension x par y.
        Pour chaque Obstacle, le mettre dans le tableau (0 pour un espace vide, 1 pour un obstacle, 2 pour un atelier, 3 pour une borne).
        """
        if not listeObstacle:
            listeObstacle = []
        if not liste_robot:
            liste_robot = []
        if not listeOuvrier:
            listeOuvrier = []

        self.listeBorne = []
        self.listeAtelier = []
        self.liste_robot = liste_robot
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

    def get_robots(self):
        """
        Retourne la liste de tout les robots sur la carte
        """
        return self.liste_robot

    def getPosRobots(self):
        """
        Retourne l'ensemble des cases prises par les robots
        """
        res = []
        for robot in self.liste_robot:
            res.append(robot.pos)
        return res

    def ajouter_robot(self, transport:bool, assemblage:bool, pos: tuple, vitesse: int = 2):
        """
        Ajoute un robot à la carte.
        """
        id_robot = len(self.liste_robot)
        self.liste_robot.append(Robot(id_robot, transport , assemblage, pos, (self.x, self.y), vitesse))

    def supprimerRobot(self,idRobot:int):
        """
        Supprime un robot de l'environnement
        """
        res = -1
        i = 1
        #ON CHERCHE LE ROBOT DANS LA CARTE
        while i<len(self.liste_robot) and res != idRobot:
            if self.liste_robot[i].getId() == idRobot:
                res = i
            i+=1
        if i != -1:
            #ON SUPPRIME LE ROBOT DE LA CARTE
            self.liste_robot.pop(res)
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

    def get_pos_impossible(self):
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

        for robot in self.liste_robot:
            if robot == -1:
                #  Robot.choix_taches retourne 1 si il est en atente
                nb_afk += robot.choix_taches()
            else:
                robot.faireTache()

        return nb_afk == len(self.liste_robot)


    def deplacer_robot(self, robot:Robot, ):
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

    def cheminement(self, debut, fin):
        """
        Renvoie un chemin entre deux points
        :param debut: Position de départ en (x, y)
        :param fin: Position de fin en (x, y)
        :return: voie de type chemin entre debut et fin
        """
        bloques = self.get_pos_impossible()
        if debut in bloques:
            bloques.remove(debut)
        if fin in bloques:
            bloques.remove(fin)

        voie = Chemin((self.x, self.y), debut, fin, bloques)
        return voie

    def choix_taches(self, liste_taches, liste_obstacles):
        """
        Le robot cherche dans la base de donnée une tâche qu'il peut faire avec ses compétences. Si c'est une tâche simple, premier arrivée , premier servi.
        (Pour le moment on s'occupe pas d'enchère , on voit après). Retourne une tâche, si aucune tâche n'est disponible/accessible, retourne False.
        TODO méthode allerA()
        """

        #  Récupère les tâches faisables par le robot.(compétence et autonomie)
        #  S'il peut en faire une , il la choisit. Retourne false si aucune tache n'est disponible
        liste_taches = sorted(liste_taches, key=lambda a: heuristic(a.depart, self.pos))
        choix = True

        # Détermine le chemin pour y aller
        while choix:
            cur_tache = liste_taches.pop()
            self.getDistance(self.limites, self.pos, cur_tache.depart, liste_obstacles)

    def getDistance(self, taille, debut, fin, list_obstacle):
        """
        Retourne le nombre de cases à parcourir pour aller à un équipement
        ou une borne. Attention, juste le nombre , pas le chemin à parcourir.
        Instancie un Chemin puis retounne le nombre de cases à parcourir
        """
        voie = Chemin(taille, debut, fin, list_obstacle)
        return int(voie)

if __name__ == '__main__':
    carte_test = Carte("Carte test", 10, 10)
    carte_test.ajouter_robot(True, True, (1, 1), 2)
    chemin = carte_test.cheminement(carte_test.get_robots()[0].pos, (5, 5))
    chemin2 = carte_test.cheminement((5, 5), (1, 1))


