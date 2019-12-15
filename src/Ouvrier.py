class Ouvrier:
    def __init__(self, pos_init:tuple, radius:int):
        #TODO AUTO INCREMENTATION ID OUVRIER
        self.pos_init = pos_init  # tuple (x,y), position initiale (fixe)
        self.pos = pos_init  # tuple (x,y), position en temps réel, amenée à changer
        self.radius = radius  # int, rayon correspondant à la limite de déplacement de l'ouvrier
        self.vit_marche = 1



    def get_pos(self):
        """
        Retourne la position actuelle de l'ouvrier (tuple)
        :return:
        """
        return self.pos

    def get_pos_init(self):
        """
        Retourne la position initiale de l'ouvrier (tuple)
        :return:
        """
        return self.pos_init

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
        radius = self.get_radius()
        x0 = self.get_pos_init()[0]
        xf = pos[0]
        y0 = self.get_pos_init()[1]
        yf = pos[1]
        return ((x0 - rad <= x0 + xf <= x0 + rad)
                and (y0 - rad <= y0 + yf <= y0 + rad))

    def se_deplacer(self,pos:tuple):
        """
        Déplace l'ouvrier aléatoirement dans son radius
        """
        self.pos = pos
