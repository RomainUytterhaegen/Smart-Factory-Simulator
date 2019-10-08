class Carte:

    def __init__(self,listeObstacle:list,x:int,y:int):
        """
        Crée un tableau de dimension x par y.
        Pour chaque Obstacle, le mettre dans le tableau (0 pour un espace vide, 1 pour un obstacle, 2 pour un équipement, 3 pour une borne).
        """
        self.listeObstacle = listeObstacle
        self.x = x
        self.y = y
        

        
        
