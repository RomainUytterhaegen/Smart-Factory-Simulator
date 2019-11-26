class Obstacle:

    ID_OBSTACLE = 1
    def __init__(self, pos1: tuple, pos2: tuple):
        #TODO AUTO INCREMENTATION ID OBSTACLE
        self.pos1 = pos1  # tuple (x1,y1)
        self.pos2 = pos2  # tuple (x2,y2)
    
    def get_id(self):
        """
        Retourne l'id d'un obstacle
        """
        return self.id_obstacle

    def get_pos1(self):
        """
        Retourne les coordonnées du coin haut_gauche de l'obstacle
        :return: Tuple
        """
        return self.pos1

    def get_pos2(self):
        """
        Retourne les coordonnées du coin bas_droit de l'obstacle
        :return: Tuple
        """
        return self.pos2

    def get_height(self):
        """
        Retourne la hauteur de l'obstacle (axe Y)
        :return: Int
        """
        return (self.pos2[1]-self.pos1[1])+1

    def get_width(self):
        """
        Retourne la largeur de l'obstacle (axe X)
        :return: Int
        """
        return (self.pos2[0]-self.pos1[0])+1
