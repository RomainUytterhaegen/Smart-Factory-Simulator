import time

class Chronometre:
    def start(self):
        """
        Lance le chronomètre (initialise le temps de départ)
        """
        if hasattr(self,'interval'):
            del self.interval
        self.start_time = time.time()
    
    def currentTime(self):
        """
        Retourne le temps actuel du chronomètre
        """
        if hasattr(self,'start_time'):
            res = time.time() - self.start_time
        else:
            raise Exception("Le Chronomètre n'est pas initialisé.")
        return res

    def stop(self):
        if hasattr(self,'start_time'):
            self.interval = time.time() - self.start_time
            del self.start_time