from Borne import Borne
from Atelier import Atelier
# from Ouvrier import Ouvrier
from Obstacle import Obstacle
from Robot import Robot
from Ouvrier import Ouvrier
from random import choice
from Chemin import Chemin, heuristic
from sys import stderr


class Carte:

    def __init__(self, nom: str, x: int, y: int,
                 liste_obstacle: list = None, liste_robot: list = None, liste_ouvrier: list = None):
        """
        Objet carte enregistrable et instancié dans simulateur. Ne doit pas être importé dans les autres classes
        :param nom: Nom de la carte par défault lors de l'enregistrement
        :param x: taille sur l'axe x (width)
        :param y: taille sur l'axe y (height)
        :param liste_obstacle: Liste contenant les objets obstacles
        #  Je suggère de faire des listes ateliers et autres
        :param liste_robot: Liste des robots
        :param liste_ouvrier: liste des ouvriers
        """
        if not liste_obstacle:
            liste_obstacle = []
        if not liste_robot:
            liste_robot = []
        if not liste_ouvrier:
            liste_ouvrier = []

        self.liste_borne = []
        self.liste_atelier = []
        self.liste_robot = liste_robot
        self.nom = nom
        self.liste_obstacle = liste_obstacle
        self.liste_ouvrier = liste_ouvrier
        self.liste_tache = []
        
        self.x = x
        self.y = y

        for i in range(0, len(self.liste_obstacle)):
            self.ajouter_obstacle(liste_obstacle[i])

    def get_obstacles(self):
        """
        Retourne tout les obstacles
        """
        return self.liste_obstacle

    def get_pos_obstacles(self):
        """
        Retourne l'ensemble des cases prises par les Obstacles.
        """
        res = []
        for obstacle in self.liste_obstacle:
            for i in range(obstacle.get_pos1()[1], obstacle.get_pos2()[1]):
                for j in range(obstacle.get_pos1()[0], obstacle.get_pos2()[0]):
                    res.append((i, j))
        return res

    def ajouter_obstacle(self, pos1: tuple, pos2: tuple):
        """
        Méthode qui ajoute un obstacle à la Carte.
        """
        pass

    def supprimer_obstacle(self, id_obstacle: int):
        """
        Méthode qui supprime un obstacle de la Carte.
        """
        res = -1
        i = 1
        # ON CHERCHE L'OBSTACLE DANS LA CARTE
        while i < len(self.liste_obstacle) and res != id_obstacle:
            if self.liste_obstacle[i].get_id() == id_obstacle:
                res = i
            i += 1
        if i != -1:
            # ON SUPPRIME L'OBSTACLE DE LA CARTE
            self.liste_obstacle.pop(res)
        else:
            # CAS OÙ L'OBSTACLE N'EST PAS DANS LA CARTE
            raise EnvironmentError("Il n'y a pas cet objet sur la carte.")

    def get_robots(self):
        """
        Retourne la liste de tout les robots sur la carte
        """
        return self.liste_robot

    def get_pos_robots(self):
        """
        Retourne l'ensemble des cases prises par les robots
        """
        res = []
        for robot in self.liste_robot:
            res.append(robot.pos)
        return res

    def ajouter_robot(self, transport: bool, assemblage: bool, pos: tuple, vitesse: int = 2):
        """
        Ajoute un robot à la carte.
        """
        #id_robot = len(self.liste_robot)
        self.liste_robot.append(Robot(transport, assemblage, pos, (self.x, self.y), vitesse))

    def supprimer_robot(self, id_robot: int):
        """
        Supprime un robot de l'environnement
        """
        res = -1
        i = 1
        # ON CHERCHE LE ROBOT DANS LA CARTE
        while i < len(self.liste_robot) and res != id_robot:
            if self.liste_robot[i].get_id() == id_robot:
                res = i
            i += 1
        if i != -1:
            # ON SUPPRIME LE ROBOT DE LA CARTE
            self.liste_robot.pop(res)
        else:
            # CAS OÙ LE ROBOT N'EST PAS DANS LA CARTE
            raise EnvironmentError("Il n'y a pas cet objet sur la carte.")

    def get_ateliers(self):
        """
        Retourne la liste des ateliers
        """
        return self.liste_atelier

    def get_pos_ateliers(self):
        """
        Retourne l'ensemble des positions prises par les ateliers
        """
        res = []
        for atelier in self.liste_atelier:
            for i in range(atelier.getPos1()[1], atelier.getPos2()[1]):
                for j in range(atelier.getPos1()[0], atelier.getPos2()[0]):
                    res.append((i, j))
        return res

    def ajouter_atelier(self, atelier: Atelier):
        """
        Ajoute un atelier à la Carte
        """
        # GERER LE CAS OÙ L'ATELIER NE PEUT PAS ÊTRE POSÉ

    def supprimer_atelier(self, id_atelier: int):
        """
        Supprime un robot de l'environnement
        """
        res = -1
        i = 1
        # ON CHERCHE L'OBSTACLE DANS LA CARTE
        while i < len(self.liste_atelier) and res != id_atelier:
            if self.liste_atelier[i].get_id() == id_atelier:
                res = i
            i += 1
        if i != -1:
            # ON SUPPRIME L'OBSTACLE DE LA CARTE
            self.liste_atelier.pop(res)
        else:
            # CAS OÙ L'OBSTACLE N'EST PAS DANS LA CARTE
            raise EnvironmentError("Il n'y a pas cet objet sur la carte.")
    
    def get_bornes_vides(self):
        """
        retourne les Bornes de la Carte
        """
        return list(filter(lambda a: a.used, self.liste_borne))

    def get_pos_bornes(self):
        """
        Retourne l'ensemble des positions prises par les bornes.
        """
        res = []
        for borne in self.liste_borne:
            res.append(borne.getPos1())
        return res

    def ajouter_borne(self, borne: Borne):
        """
        Ajoute une Borne dans la Carte
        """
        # GERER SI ON PEUT POSER LA BORNE
        pass

    def supprimer_borne(self, id_borne: int):
        """
        Supprime une Borne de la Carte
        """
        res = -1
        i = 1
        # on CHERCHE LA BORNE DANS LA CARTE
        while i < len(self.liste_borne) and res != id_borne:
            if self.liste_borne[i].get_id() == id_borne:
                res = i
            i += 1
        if i != -1:
            # ON SUPPRIME LA BORNE DE LA CARTE
            self.liste_borne.pop(res)
        else:
            # CAS OÙ LA BORNE N'EST PAS DANS LA CARTE
            raise EnvironmentError("Il n'y a pas cet objet sur la carte.")

    def chemin_borne_proche(self, pos:tuple):
        liste_bornes = sorted(self.get_bornes_vides(), key=lambda a: heuristic(a.depart, pos))
        choix = True

        try:
            plus_proche = liste_bornes[0].pos1
        except IndexError:
            print("La liste des bornes est vide", file=stderr)
            return 0, 0

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
        return self.get_pos_ateliers() + self.get_pos_obstacles() + self.get_pos_robots() + self.get_pos_bornes()

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
    def get_voisins(pos:tuple):
        """
        Retourne la liste des cases voisines d'une case
        :param pos:
        :return:
        """
        x, y = pos
        return [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]

    def case_occupee(self, pos:tuple):
        return pos in self.get_obstacles()

    def deplace_ouvrier(self, ouv: Ouvrier):
        """
        Déplace l'ouvrier d'une case disponible, à sa portée et dans son rayon de déplacement
        :param ouv: Ouvrier que l'on souhaite déplacer
        """
        ouv.se_deplacer(choice(filter(self.case_occupee, list(filter(ouv.in_radius, self.get_voisins(ouv.get_pos()))))))

    def cheminement(self, debut:tuple, fin:tuple):
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

    def choix_taches(self, robot: Robot):
        """
        Choisi une tâche et l'affecte au robot
        :param robot: Robot à qui affecter une tache
        :return: 0 si l'opération a été effectuée 1 sinon
        """
        liste_taches = sorted(self.liste_tache, key=lambda a: heuristic(a.depart, robot.pos))
        choix = True

        while choix and len(liste_taches) > 0:
            cur_tache = liste_taches.pop()
            dist = self.get_distance(robot.pos, cur_tache.depart)
            if dist >= 1:
                robot.tache = cur_tache
                choix = False
        return int(choix)

    def get_distance(self, debut:tuple, fin:tuple):
        """
        Retourne le nombre de cases à parcourir pour aller à un équipement
        ou une borne. Attention, juste le nombre , pas le chemin à parcourir.
        Instancie un Chemin puis retounne le nombre de cases à parcourir
        """
        return int(self.cheminement(debut, fin))


if __name__ == '__main__':
    carte_test = Carte("Carte test", 10, 10)
    carte_test.ajouter_robot(True, True, (1, 1), 2)
    chemin_t = carte_test.cheminement(carte_test.get_robots()[0].pos, (5, 5))
    chemin2_t = carte_test.cheminement((5, 5), (1, 1))
    print(chemin_t)
    print(chemin2_t)
