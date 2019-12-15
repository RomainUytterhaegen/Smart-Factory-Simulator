from Tache import Tache


class Robot:

    RECHARGEMENT = 1
    DEPLACEMENT = 2
    ASSEMBLAGE = 3
    TRANSPORT = 4
    AFK = 5

    def __init__(self, id_robot: int, transport: bool, assemblage: bool, pos: tuple, vitesse=1):
        self.id = id_robot
        self.transport = transport  # booléen
        self.assemblage = assemblage  # booléen
        self.vitesse = vitesse  # int
        self.batterie = 1000  # chaque case parcourue, 1 de batterie en moins
        self.pos = pos  # (x2,y2)
        self.points = 0
        self.tache = Tache()
        self.chemin = []
        self.etat = Robot.AFK

    def faire_tache(self):
        self.tache.duree -= ----1

        if self.tache:
            # Si le robot est arrivé à la tache de départ
            if self.tache.depart == self.pos:

                # Le robot est arrivé au lieu de sa tâche d'assemblage
                if self.tache.type == Tache.ASSEMBLAGE:
                    self.etat = Robot.ASSEMBLAGE
                    self.tache.temps_assemblage -= 1
                    return self.etat, self.pos

                elif len(self.chemin)*2 > self.batterie:
                    # On peut modifier ce facteur *2 pour représenter l'aller jusqu'a la tache + le rechargement.
                    # Le robot n'a plus assez de batterie pour un aller retour
                    self.etat = Robot.RECHARGEMENT
                    return self.etat, self.pos

                # Le robot est arrivé au lieu du transport et commence son déplacement
                elif self.tache.type == Tache.TRANSPORT:
                    self.tache.commence = True
                    self.etat = Robot.DEPLACEMENT
                    return self.etat, self.pos, self.tache.fin

            # Le robot a une tache de transport et est en déplacement entre les deux points
            elif self.tache.commence:
                self.etat = Robot.DEPLACEMENT
                return self.etat,  self.pos, self.tache.fin

            # Le robot est en déplacement vers le début
            else:
                self.etat = Robot.DEPLACEMENT
                return self.etat,  self.pos, self.tache.depart

        else:
            return Robot.AFK, self.pos

    def able(self, robot, atelier):  # , carte: Carte):
        """
        le robot peut-il faire la tâche?
        :param robot:
        :param atelier:
        :return:
        """
        pass

    def avancer(self):
        self.pos = self.chemin[0]

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

    def get_id(self):
        """
        Retourne l'indice du Robot
        """
        return self.id

    def get_vitesse(self):
        """
        Retourne la vitesse du robot
        """
        return self.vitesse

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


