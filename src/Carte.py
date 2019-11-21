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
            if self.listeObstacle[i].get_id() == idObstacle:
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
            if self.liste_robot[i].get_id() == idRobot:
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
            if self.listeAtelier[i].get_id() == idAtelier:
                res = i
            i+=1
        if i != -1:
            #ON SUPPRIME L'OBSTACLE DE LA CARTE
            self.listeAtelier.pop(res)
        else:
            #CAS OÙ L'OBSTACLE N'EST PAS DANS LA CARTE
            raise EnvironmentError("Il n'y a pas cet objet sur la carte.")
    
    def get_bornes_vides(self):
        """
        retourne les Bornes de la Carte
        """
        return list(filter(lambda a: a.used, self.listeBorne))

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

    def supprimer_borne(self, idBorne:int):
        """
        Supprime une Borne de la Carte
        """
        res = -1
        i = 1
        # on CHERCHE LA BORNE DANS LA CARTE
        while i<len(self.listeBorne) and res != idBorne:
            if self.listeBorne[i].get_id() == idBorne:
                res = i
            i+=1
        if i != -1:
            # ON SUPPRIME LA BORNE DE LA CARTE
            self.listeBorne.pop(res)
        else:
            # CAS OÙ LA BORNE N'EST PAS DANS LA CARTE
            raise EnvironmentError("Il n'y a pas cet objet sur la carte.")

    def chemin_borne_proche(self, pos):
        liste_bornes = sorted(self.get_bornes_vides(), key=lambda a: heuristic(a.depart, pos))
        choix = True

        plus_proche = liste_bornes[0].pos1

        while choix and len(liste_bornes) > 0:
            borne = liste_bornes.pop()
            chemin = self.cheminement(pos, borne.pos1)
            if int(chemin) >= 1:
                return chemin
        return self.cheminement(pos, plus_proche)  # todo modifier pour mettre une case voisine

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
            if robot.tache == -1:
                #  choix_taches retourne 1 si il est en atente
                nb_afk += self.choix_taches(robot)
            action = robot.faire_tache()

            if action[0] == Robot.RECHARGEMENT:

                robot.chemin = self.chemin_borne_proche(action[1])
            elif action[0] == Robot.ASSEMBLAGE:
                pass
            elif action[0] == Robot.TRANSPORT:
                pass

        return nb_afk == len(self.liste_robot)

    def deplacer_robot(self, robot: Robot):
        pass

    @staticmethod
    def get_voisins(pos):
        """
        Retourne la liste des cases voisines d'une case
        :param pos:
        :return:
        """
        x, y = pos
        return [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]

    def case_occupee(self, pos):
        return pos in self.getObstacles()

    def deplaceOuvrier(self, ouv:Ouvrier):
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

    def choix_taches(self, robot):
        """
        Choisi une tâche et l'affecte au robot
        :param robot: Robot à qui affecter une tache
        :return: 0 si l'opération a été effectuée 1 sinon
        """
        liste_taches = sorted(self.listeTache, key=lambda a: heuristic(a.depart, robot.pos))
        choix = True

        while choix and len(liste_taches) > 0:
            cur_tache = liste_taches.pop()
            dist = self.get_distance(robot.pos, cur_tache.depart)
            if dist >= 1:
                robot.tache = cur_tache
                choix = False
        return int(choix)

    def get_distance(self, debut, fin):
        """
        Retourne le nombre de cases à parcourir pour aller à un équipement
        ou une borne. Attention, juste le nombre , pas le chemin à parcourir.
        Instancie un Chemin puis retounne le nombre de cases à parcourir
        """
        return int(self.cheminement(debut, fin))


if __name__ == '__main__':
    carte_test = Carte("Carte test", 10, 10)
    carte_test.ajouter_robot(True, True, (1, 1), 2)
    chemin = carte_test.cheminement(carte_test.get_robots()[0].pos, (5, 5))
    chemin2 = carte_test.cheminement((5, 5), (1, 1))
