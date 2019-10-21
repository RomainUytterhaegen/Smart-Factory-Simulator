from Obstacle import Obstacle
from Tache import Tache

class Atelier(Obstacle):
    def __init__(self,id:int,pos1:tuple,pos2:tuple,utilite:str):
        Obstacle.__init__(self,id,pos1,pos2)
        if self.ulilite in ["Assemblage","Transport"]:
            self.utilite = utilite
        else:
            #Faut lancer une exception
            pass

    def getUtilite(self):
        """
        Retourne l'utilité de l'atelier
        """
        return self.utilite
    
    def genererTache(self):
        """
        Génère une tâche lorsqu'elle est appelée.
        """
        tache = Tache()
        return tache