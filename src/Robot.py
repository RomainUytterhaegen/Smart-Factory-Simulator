from Tache import Tache


class Robot:

    RECHARGEMENT = 1
    DEPLACEMENT = 2
    ASSEMBLAGE = 3
    TRANSPORT = 4
    ID_ROBOT = 1

    def __init__(self, transport: bool, assemblage: bool, pos: tuple, limite: tuple, vitesse=2):
        #TODO AUTO INCREMENTATION ID ROBOT
        self.id_robot = self.ID_ROBOT
        self.ID_ROBOT += 1 
        self.transport = transport  # booléen
        self.assemblage = assemblage  # booléen
        self.vitesse = vitesse  # int
        self.batterie = 1000  # chaque case parcourue, 1 de batterie en moins
        self.pos = pos  # (x2,y2)
        self.limites = limite  # Limite de la carte pour ne pas avoir à l'importer
        self.points = 0
        self.tache = Tache()
        self.chemin = []

    def faire_tache(self):
        if self.tache:
            if self.tache.depart == self.pos:
                if len(self.chemin)*2 > self.batterie:
                    # On peut modifier ce facteur *2 pour représenter l'aller jusqu'a la tache + le rechargement.
                    return Robot.RECHARGEMENT, self.pos
                elif self.tache.type == "Assemblage":
                    return Robot.ASSEMBLAGE, self.pos
                elif self.tache.type == "Transport":
                    return Robot.TRANSPORT, self.pos, self.tache.fin
        else:
            return Robot.RECHARGEMENT, self.pos

    # def aller_borne(self):
    #     """
    #     Trouve une borne qui n'est pas occupée, détermine le Chemin pour y aller, puis s'y dirige.
    #     retourne False si aucune borne n'est disponible
    #     """
    #
    #     #  ON RECUPERE TOUTES LES BORNES DISPONIBLES
    #     bornes_dispo = {}
    #     for borne in carte.listeBorne:
    #         bornes_dispo[borne.id] = self.get_distance(borne,carte)
    #
    #     #ON CHERCHE LAQUELLE EST LA PLUS PROCHE
    #     la_borne = min(bornes_dispo.items(), key=lambda x: x[1])
    #
    #     # ON DIRIGE LE ROBOT JUSQU'A LA BORNE ET IL SE RECHARGE
    #     for borne_1 in carte.listeBorne:
    #         if la_borne[0] == borne_1.id:
    #             self.aller_a(borne_1,carte)
    #             borne_1.recharge(self)

    def get_id(self):
        """
        Retourne l'indice du Robot
        """
        return self.id_robot

    def get_autonomie(self):
        """
        Retourne la distance que peut faire le robot avant de tomber en panne
        """
        return self.batterie
    
    def get_competences(self):
        """
        Retourne les compétences du robot sous forme d'un tableau booléen
        suivant : [transport,assemblage]
        """
        return [self.transport, self.assemblage]

    def get_vitesse(self):
        """
        Retourne la vitesse du robot
        """
        return self.vitesse

    # def aller_a(self):
    #     """
    #     Déplace le robot jusqu'à un point donné. Vérifie qu'il avance une case par une(voir code ci-dessous)
    #
    #     """
    #     #INSTANCIE UN CHEMIN
    #     voie = Chemin((carte.x,carte.y),self.pos,obstacle.pos1,carte.listeObstacle)
    #
    #     #DEPLACE LE ROBOT EN SUIVANT LE CHEMIN
    #     while len(voie.chemin)>1:
    #         x = voie.chemin[0][0]
    #         y = voie.chemin[0][1]
    #         if carte.plan[x][y] == 0:
    #             self.pos = voie.chemin[0]
    #             voie.chemin.pop(0)
    #
    # def pour_combien(self):
    #     """
    #     Le robot estime son prix minimal pour être payé(en fonction de sa distance,
    #     ses compétences, vitesse , ect), il propose un prix en fonction de ce calcul.
    #     le reste sera géré par la classe TacheEnchere.
    #     """
    #     return self.get_distance(tache, carte)*self.vitesse + tache.duree()

    def is_full(self):
        """
        Retourne TRUE si la batterie du Robot est chargée , false sinon
        """
        return self.batterie == 1000

    def remplir_batterie(self, recharge: float):
        """
        Recharge la batterie d'une certaine quantité
        """
        self.batterie += recharge

    def able(self, robot, atelier):  # , carte: Carte):
        """
        le robot peut-il faire la tâche?
        :param robot:
        :param atelier:
        :return:
        """
        pass
