from Borne import Borne
from Atelier import Atelier
# from Ouvrier import Ouvrier
from Obstacle import Obstacle
from Robot import Robot
from Ouvrier import Ouvrier
from random import choice
from Chemin import Chemin, heuristic
from sys import stderr
from Tache import Tache


class Carte:

    def __init__(self, nom: str, x: int, y: int, liste_obstacle: list = None, liste_robot: list = None,
                 liste_atelier: list = None, liste_ouvrier: list = None, liste_borne: list = None):
        """
        Objet carte enregistrable et instancié dans simulateur. Ne doit pas être importé dans les autres classes
        :param nom: Nom de la carte par défault lors de l'enregistrement
        :param x: taille sur l'axe x (width)
        :param y: taille sur l'axe y (height)
        :param liste_obstacle: Liste contenant les objets obstacles
        :param liste_atelier: Liste contenant les ateliers
        :param liste_robot: Liste des robots
        :param liste_ouvrier: liste des ouvriers
        """
        if not liste_obstacle:
            self.liste_obstacle = []
        else:
            self.liste_obstacle = liste_obstacle

        if not liste_robot:
            self.liste_robot = []
        else:
            self.liste_robot = liste_robot

        if not liste_atelier:
            self.liste_atelier = []
        else:
            self.liste_atelier = liste_atelier

        if not liste_ouvrier:
            self.liste_ouvrier = []
        else:
            self.liste_ouvrier = liste_ouvrier

        if not liste_borne:
            self.liste_borne = []
        else:
            self.liste_borne = liste_borne
        self.nom = nom
        self.liste_tache = []

        self.x = x
        self.y = y

    def ajouter_atelier(self, pos1: tuple, pos2: tuple):
        """
        Ajoute un atelier à la Carte
        """
        id_at = len(self.liste_atelier)
        self.liste_atelier.append(Atelier(id_at, pos1, pos2))

    def ajouter_borne(self, pos: tuple):
        """
        Ajoute une Borne dans la Carte
        """
        id_borne = len(self.liste_borne)
        self.liste_borne.append(Borne(id_borne, pos))

    def ajouter_obstacle(self, pos1: tuple, pos2: tuple):
        """
        Méthode qui ajoute un obstacle à la Carte.
        :param pos1: coin en haut à gauche
        :param pos2: coin en bas à droite
        """
        self.liste_obstacle.append(Obstacle(len(self.liste_obstacle), pos1, pos2))

    def ajout_tache(self, pos_deb: tuple, pos_fin=(-1, -1)):
        if pos_fin == (-1, -1):
            self.liste_tache.append(Tache(pos_depart=pos_deb))
        else:
            self.liste_tache.append(Tache(pos_depart=pos_deb, pos_fin=pos_fin))

    def ajout_tache_atelier(self, id_atelier, temps: int):
        try:
            atelier = self.find_atelier(id_atelier)
            atelier.gen_tache(atelier.pos1, temps)
        except ValueError:
            print(f"Aucune Tâche ne peut être assigné à l'atelier numéro {id_atelier}")

    def ajouter_robot(self, transport: bool, assemblage: bool, pos: tuple, vitesse: int = 2):
        """
        Ajoute un robot à la carte.
        """
        id_robot = len(self.liste_robot)
        self.liste_robot.append(Robot(id_robot, transport, assemblage, pos, vitesse))

    def case_libre(self, pos: tuple):
        return not (pos in self.get_pos_impossible())

    def case_occupee(self, pos: tuple):
        return pos in self.get_obstacles()

    def chemin_borne_proche(self, pos: tuple):
        liste_bornes = sorted(self.get_bornes_vides(), key=lambda a: heuristic(a.pos1, pos))
        choix = True
        try:
            plus_proche = liste_bornes[0].pos1
        except IndexError:
            print("La liste des bornes est vide")
            return 0, 0

        while choix and len(liste_bornes) > 0:
            borne = liste_bornes.pop()
            chemin = self.cheminement(pos, borne.pos1)
            if int(chemin) >= 1:
                return chemin
        return self.cheminement(pos, plus_proche)  # todo modifier pour mettre une case voisine

    def cheminement(self, debut: tuple, fin: tuple):
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
        :return: 0 si une tache a été choisie 1 sinon
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

    def deplace_ouvrier(self, ouv: Ouvrier):
        """
        Déplace l'ouvrier d'une case disponible, à sa portée et dans son rayon de déplacement
        :param ouv: Ouvrier que l'on souhaite déplacer
        """
        voisins_dans_rad = list(filter(ouv.in_radius, self.get_voisins(ouv.get_pos())))
        ouv.se_deplacer(choice(list(filter(self.case_libre, voisins_dans_rad))))

    def get_ateliers(self):
        """
        Retourne la liste des ateliers
        """
        return self.liste_atelier

    def get_bornes_vides(self):
        """
        retourne les Bornes de la Carte
        """
        return list(filter(lambda a: not a.used, self.liste_borne))


    def get_distance(self, debut: tuple, fin: tuple):
        """
        Retourne le nombre de cases à parcourir pour aller à un équipement
        ou une borne. Attention, juste le nombre , pas le chemin à parcourir.
        Instancie un Chemin puis retounne le nombre de cases à parcourir
        """
        return int(self.cheminement(debut, fin))

    def get_obstacles(self):
        """
        Retourne tout les obstacles
        """
        return self.liste_obstacle

    def get_pos_ateliers(self):
        """
        Retourne l'ensemble des positions prises par les ateliers
        """
        return [(i, j) for atelier in self.liste_atelier for i in range(atelier.pos1[0], atelier.pos2[0])
                for j in range(atelier.pos1[1], atelier.pos2[1])]

    def get_pos_bornes(self):
        """
        Retourne l'ensemble des positions prises par les bornes.
        """
        return [p.pos1 for p in self.liste_borne]

    def get_pos_impossible(self):
        """
        Retourne l'ensemble des cases de l'usines non traversables
        """
        return self.get_pos_ateliers() + self.get_pos_obstacles() + self.get_pos_robots() + self.get_pos_bornes()

    def get_pos_obstacles(self):
        """
        Retourne l'ensemble des cases prises par les Obstacles.
        """
        res = []
        for obstacle in self.liste_obstacle:
            for i in range(obstacle.get_pos1()[1], obstacle.get_pos2()[1] + 1):
                for j in range(obstacle.get_pos1()[0], obstacle.get_pos2()[0] + 1):
                    res.append((j, i))
        return res

    def get_pos_robots(self):
        """
        Retourne l'ensemble des cases prises par les robots
        """
        res = []
        for robot in self.liste_robot:
            res.append(robot.pos)
        return res


    def get_taches_ateliers(self):
        return [t for atelier in self.liste_atelier for t in atelier.update_taches()]

    @staticmethod
    def get_voisins(pos: tuple):
        """
        Retourne la liste des cases voisines d'une case
        :param pos:
        :return:
        """
        x, y = pos
        return [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]

    def get_voisins_tache(self, obstacle: Obstacle):
        """
        retourne les cases voisines inocupées d'un obstacle
        :param obstacle:
        :return:
        """
        res = set()
        for i in range(obstacle.pos1[0], obstacle.pos2[0] + 1):
            res.add((i, obstacle.pos1[1] - 1))
            res.add((i, obstacle.pos2[1] + 1))
        for j in range(obstacle.pos1[1], obstacle.pos2[1] + 1):
            res.add((obstacle.pos1[0] - 1, j))
            res.add((obstacle.pos2[0] + 1, j))
        return res.difference(set(self.get_pos_impossible()))

    def get_robots(self):
        """
        Retourne la liste de tout les robots sur la carte
        """
        return self.liste_robot

    def find_atelier(self, id_atelier):
        """
        Trouve un atelier à partir d'un id. Retourne une erreur si l'id ne corresspond à rien
        :param id_atelier: Id d'un atelier à trouver
        :return: L'atelier en question
        """
        for atelier in self.liste_atelier:
            if atelier.id == id_atelier:
                return atelier
        raise ValueError

    def supprimer_atelier(self, id_atelier: int):
        """
        Supprime un atelier de l'environnement
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
            print(f"Il n'y a pas l'obstacle {id_obstacle}  sur la carte.", file=stderr)

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

    def tour_simulation(self):
        """
        Réalise un tour de simulation
        :return: True si les robots n'ont tous plus rien à faire
        """
        print("DEBUG tour simulation")

        self.liste_tache += self.get_taches_ateliers()

        for robot in self.liste_robot:
            if robot.etat == Robot.AFK:
                #  Ajouter la condition de tache fini
                self.choix_taches(robot)
                # todo faire en sorte que si le robot est afk, il prenne une tache si une nouvelle est déclarée
            action = robot.faire_tache()

            if action[0] == Robot.AFK:
                robot.chemin = self.chemin_borne_proche(action[1]).chemin
                robot.avancer()
            if action[0] == Robot.RECHARGEMENT:
                robot.chemin = self.chemin_borne_proche(action[1]).chemin
                robot.avancer()
            elif action[0] == Robot.ASSEMBLAGE:
                # Si jamais il faut faire quelque chose pendant l'assemblage
                pass
            elif action[0] == Robot.TRANSPORT:
                robot.chemin = self.cheminement(action[1], action[2]).chemin
                robot.avancer()
            elif action[0] == Robot.DEPLACEMENT:
                robot.chemin = self.cheminement(action[1], action[2]).chemin
                robot.avancer()








if __name__ == '__main__':
    carte_test = Carte("Carte test", 10, 10)
    carte_test.ajouter_robot(True, True, (1, 1), 2)
    chemin_t = carte_test.cheminement(carte_test.get_robots()[0].pos, (5, 5))
    carte_test.ajouter_obstacle((2, 1), (4, 1))
    chemin2_t = carte_test.cheminement((1, 1), (5, 5))
    carte_test.ajouter_borne((8, 8))

    print(carte_test.liste_robot[0].pos)
    carte_test.tour_simulation()
    print(carte_test.liste_robot[0].pos)
    carte_test.tour_simulation()
    print(carte_test.liste_robot[0].pos)
    carte_test.tour_simulation()
    print(carte_test.liste_robot[0].pos)
    print(carte_test.liste_robot[0].chemin)
