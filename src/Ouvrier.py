class Ouvrier:
    def __init__(self, pos_init:tuple, radius:int):
        #TODO AUTO INCREMENTATION ID OUVRIER
        self.pos_init = pos_init  # tuple (x,y), position initiale (fixe)
        self.pos = pos_init  # tuple (x,y), position en temps réel, amenée à changer
        self.radius = radius  # int, rayon correspondant à la limite de déplacement de l'ouvrier
        self.vit_marche = 1

    def get_pos_init(self):
        """
        Retourne la position initiale de l'ouvrier (tuple)
        :return:
        """
        return self.pos_init

    def get_pos(self):
        """
        Retourne la position actuelle de l'ouvrier (tuple)
        :return:
        """
        return self.pos

    def get_radius(self):
        """
        Retourne le rayon de déplacement de l'ouvrier (int)
        :return:
        """
        return self.radius

    def in_radius(self, pos:tuple):
        """
        Retourne true si la position passée en paramètre est dans le rayon de déplacement de l'ouvrier, false sinon
        :param pos:
        :return:
        """
        return ((self.get_pos_init()[0] - self.get_radius() <=
                 self.get_pos()[0] + pos[0] <= self.get_pos_init()[0] + self.get_radius())
                and self.get_pos_init()[1] - self.get_radius() <=
                self.get_pos()[1] + pos[1] <= self.get_pos_init()[1] + self.get_radius())

    def se_deplacer(self):
        """
        Déplace l'ouvrier aléatoirement dans son radius
        """
        self.pos = tup
