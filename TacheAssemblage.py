from Tache import Tache

class TacheAssemblage(Tache) :

    def __init__(self,dureeAss:int):
        Tache.__init__()
        self.dureeAss = dureeAss
        