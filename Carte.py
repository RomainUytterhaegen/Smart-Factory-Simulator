class Carte:

    def __init__(self,listeObstacle:list,x:int,y:int):
        """
        Crée un tableau de dimension x par y.
        Pour chaque Obstacle, le mettre dans le tableau (0 pour un espace vide, 1 pour un obstacle, 2 pour un atelier, 3 pour une borne).
        """
        self.listeObstacle = listeObstacle
        self.x = x
        self.y = y
        self.plan = array()
        # Création du plan vide
        for c in range(0,self.x):
            plan.append([])
            for d in range(0,self.y):
                self.plan[c].append(0)

        for i in range(0,len(self.listeObstacle)):
            if type(listeObstacle[i]) is in ("Atelier","Borne","Obstacle"):
                p1 = self.listeObstacle[i].getPos1()
                x1 = p1[0]
                y1 = p1[1]
                w = self.listeObstacle[i].getWidth()
                h = self.listeObstacle[i].getHeight()

                for k in range(x1,w):            #Le plan suit donc le sens bas_gauche vers haut_droit
                    for l in range(y1,h):

                        if type(listeObstacle[i]) == "Atelier":
                            self.plan[k][l] = 2

                        elif type(listeObstacle[i]) == "Borne":
                            self.plan[k][l] = 3

                        elif type(listeObstacle[i]) == "Obstacle":
                            self.plan[k][l] = 1