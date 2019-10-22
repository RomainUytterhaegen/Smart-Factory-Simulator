from Borne import Borne
from Atelier import Atelier
from Obstacle import Obstacle

class Carte:

    def __init__(self,x:int,y:int,listeObstacle:list = []):
        """
        Crée un tableau de dimension x par y.
        Pour chaque Obstacle, le mettre dans le tableau (0 pour un espace vide, 1 pour un obstacle, 2 pour un atelier, 3 pour une borne).
        """
        self.listeObstacle = listeObstacle
        #On supprime tout les obstacles dans la base de donnée
        self.x = x
        self.y = y
        self.plan = []
        # Création du plan vide
        for c in range(0,self.x):
            self.plan.append([])
            for d in range(0,self.y):
                self.plan[c][d].append(0)

        for i in range(0,len(self.listeObstacle)):
            self.ajouterObstacle(listeObstacle[i])

    def getObstacles(self):
        """
        Retourne toutes les cases qui ne sont pas traversables
        """
        res = []
        for i in range(self.x):
            for j in range(self.y):
                if self.plan[i][j] != 0:
                    res.append((i,j))
        return res

    def ajouterObstacle(self,obstacle:Obstacle):
        
        p1 = obstacle.getPos1()
        x1 = p1[0]
        y1 = p1[1]
        w = obstacle.getWidth()
        h = obstacle.getHeight()

        if x1+w>self.x and y1+h>self.y:
            #On ajoute l'obstacle dans la base de donnée
            for k in range(x1,w):            #Le plan suit donc le sens bas_gauche vers haut_droit
                for l in range(y1,h):

                    if type(obstacle) == "Atelier":
                        self.plan[k][l] = 2

                    elif type(obstacle) == "Borne":
                        self.plan[k][l] = 3

                    elif type(obstacle) == "Obstacle":
                        self.plan[k][l] = 1
        else:
            raise EnvironmentError("L'objet ne peut pas être placé.")

    def supprimerObstacle(self,idObstacle:int):
        res = -1
        i = 1
        while i<len(self.listeObstacle) and res != idObstacle:
            if self.listeObstacle[i].getId() == idObstacle:
                res = i
            i+=1
        if i != -1:
            #On delete l'obstacle de la base de donnée
            self.listeObstacle.pop(res)
        else:
            raise EnvironmentError("Il n'y a pas cet objet sur la carte.")

        

