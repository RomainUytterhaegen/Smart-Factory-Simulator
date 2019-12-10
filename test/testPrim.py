
def heuristic(a:tuple, b:tuple):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def creer_graphe(*tuples):
    """
    Créer un graphe non orientée en matrice à partir des positions passées en paramètres.
    Premier tuple : lieu de départ
    Dernier tuple : lieu d'arrivée
    :param tuples:
    :return:
    """

    #INITIALISATION MATRICE A 0
    graphe = [[0 for column in range(len(tuples))]
                    for row in range(len(tuples))]

    #REMPLISSAGE DES POIDS DE LA MATRICE
    for i in range(len(tuples)):
        for j in range(len(tuples)):
            if i != j:
                graphe[i,j] = heuristic(tuples[i],tuples[j])

    return graphe

def indice_min(liste:list):
    imin = 0
    for i in range(len(liste)):
        if liste[imin] > liste[i]:
            imin = i
    return imin

def est_complet(graphe:list):
    res = True
    for i in range(len(graphe)):
        if sum(graphe[i]) <= 0:
            res = False
    return res

test = [[0,4,25,1],
        [2,0,6,1],
        [2,6,0,24],
        [2,1,2,0],
        ]

def min_spanning_tree(graphe:list):
    """
    Créer l'arbre de poids minimum du graphe, ce qui permet dde déterminer le chemin le plus optimisé.
    :param graphe:
    :return:
    """
    racine = 0

    res = [[0 for column in range(len(tuples))]
              for row in range(len(tuples))]





    pass

