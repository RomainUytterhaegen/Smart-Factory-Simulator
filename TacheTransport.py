from Tache import Tache

class TacheTransport(Tache) :

    def __init__(self,dureeChargmt:int):
        Tache.__init__()
        self.dureeChargmt = dureeChargmt