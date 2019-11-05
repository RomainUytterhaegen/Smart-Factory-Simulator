import heapq
import sys

"""
Voir le code original dans astar_sample_code.py
Seulement Chemin est utilisé dans les autres pages
"""


class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bounds(self, pos):
        (x, y) = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, pos):
        return pos not in self.walls

    def neighbors(self, pos):
        try:
            (x, y) = pos
        except ValueError:
            print("Erreur:", pos)
            raise ValueError
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return list(results)


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph: SquareGrid, start: tuple, goal: tuple):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for prochain_point in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if prochain_point not in cost_so_far or new_cost < cost_so_far[prochain_point]:
                cost_so_far[prochain_point] = new_cost
                priority = new_cost + heuristic(goal, prochain_point)
                frontier.put(prochain_point, priority)
                came_from[prochain_point] = current

    current = goal
    path = []
    while current != start:
        path.append(current)
        try:
            current = came_from[current]
        except TypeError:
            print(current, start, goal, type(came_from), type(current), sep='\n', file=sys.stderr)
            raise KeyError
    path.reverse()
    return path


def a_star(tgrille: list, depart: tuple, fin: tuple, pos_murs: list)->list:
    """
    Algorithme à utiliser pour une recherche de chemin. Trouve l'un des plus court chemins sur un plateau.
    La Partie recherche se trouve dans a_star_search()
    Ici il n'y a que les tests pour ne pas faire d'erreur
    :param pos_murs: position des obstacles.
    :param tgrille: Taille plateau de jeu sous forme de tuple (y, x) ou (len(grille), len(grille[0])).
    :param depart: tuple avec l'emplacement de départ sous forme (x, y).
    :param fin: tuple avec l'emplacement d'arrivée sous forme (x, y).
    :return: liste des cases parcourues jusqu'à l'objectif.
    """
    long, larg = tgrille

    pos_murs = list(set(pos_murs))

    grille_jeu = SquareGrid(long, larg)
    grille_jeu.walls = pos_murs
    return a_star_search(grille_jeu, depart, fin)


def plus_proche_search(graph: SquareGrid, start: tuple, objectifs: list):
    """
    Algorithme trouvant l'objectif le plus proche
    :param graph: Grille du plateau
    :param start: tuple (x, y) de départ
    :param objectifs: Liste des tuples d'objectifs
    """
    visitees = []
    a_faire = []
    predesseceurs = {}
    cost_sofar = {start: 0}

    position = start

    while position not in objectifs:
        visitees.append(position)
        for p in graph.neighbors(position):
            if p not in visitees:
                a_faire.append(p)
                predesseceurs[p] = position

        # La distance pour aller jusqu'à ce point
        try:
            position = a_faire.pop(0)
            cost_sofar[position] = cost_sofar[predesseceurs[position]]+1
        except IndexError:
            return False
        except KeyError:
            print("\nErreur", file=sys.stderr)
            print(visitees, a_faire, cost_sofar, predesseceurs, position, sep="\n", file=sys.stderr)
            return False

    return position, cost_sofar[position]


class PlusProche:

    distance = 0
    proche = (0, 0)

    def __init__(self, taille_grille: tuple, debut: tuple, objectifs: list, murs=None):
        """
        Permet de définir l'objectif le plus proche et sa distance
        :param taille_grille: taille de la grille (hauteur, longueur)
        :param debut: position de départ (x, y)
        :param objectifs: Liste avec les positions d'arrivées
        :param murs: Si il y a des murs, une liste qui les contient
        """
        if not murs:
            murs = []

        w, h = taille_grille
        grid = SquareGrid(w, h)
        grid.walls = murs

        resultat = plus_proche_search(grid, debut, objectifs)
        if resultat:
            self.proche, self.distance = resultat
        else:
            self.proche = debut
            self.distance = taille_grille[0]*taille_grille[1]


class Chemin:
    """
    Classe qui trouve un chemin entre deux position.
    """

    distance = 0
    deb = 0, 0
    fin = 0, 0
    chemin = []
    cur = 0

    def __init__(self, taille_grille, debut: tuple, fin: tuple, murs=None):
        if murs is None:
            murs = list()

        self.deb = debut
        self.fin = fin

        if debut in murs:
            raise ValueError(f"La position de départ est dans un obstacle. dep:{debut} fin:{fin}")
        if fin in murs:
            raise ValueError(f"La position d'arrivée est dans un obstacle. dep:{debut} fin:{fin}")

        try:
            if debut != fin:
                self.chemin = a_star(taille_grille, debut, fin, murs)
            else:
                self.chemin = [debut]
            self.distance = len(self.chemin)
        except KeyError:
            # l'objet est inateignable
            self.distance = taille_grille[0]*taille_grille[1]
            self.chemin = [debut]

    def get_next(self):
        self.cur += 1
        return self.chemin[self.cur-1]

    def __int__(self):
        return self.distance
