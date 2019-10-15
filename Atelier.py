from Obstacle import Obstacle

class Atelier(Obstacle):
    def __init__(self,id,pos1,pos2,utilite):
        Obstacle.__init__(self,id,pos1,pos2)
        self.utilite = utilite

    def getUtilite(self):
        """
        Retourne l'utilité de l'atelier
        """
        return self.utilite
    
    def genereTache(self):
        """
        Génère une tâche
        :return: Tache
        """
        pass