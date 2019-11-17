from Carte import Carte
from threading import Thread
from time import sleep


class Simulateur:

    def __init__(self, carte=Carte("Carte par défaut", 10, 10)):
        """
        Initialise l'usine et la simulation
        """
        self.carte_main = carte
        self.carte_init = carte

        self.etat = False
        self.vitesse = 0.5

        self.val_test = 1

    def lancer(self):
        """
        Lance la simulation, a utiliser dans un thread sinon création de boucle infinie
        """
        self.etat = True
        fini = False

        while self.etat and not fini:
            fini = self.carte_main.tour_simulation()
            sleep(self.vitesse)

        if fini:
            print("Tous les robots on finis")

    def pauser(self):
        """
        Pause la simulation
        :return:
        """
        self.etat = False

    def reinitialiser(self):
        """
        Remet la simulation à zero et réinitialise les attributs
        :return:
        """
        self.etat = False
        self.carte_main = self.carte_init


if __name__ == '__main__':

    sim_test = Simulateur()
    sim_test.carte_main.ajouterRobot(True, True, (0, 0), 2)

    main_t = Thread(target=sim_test.lancer, args=(sim_test.etat, sim_test.vitesse))
    main_t.run = sim_test.lancer

    print(sim_test.val_test)
    main_t.start()

    sleep(2)
    sim_test.pauser()

    print(sim_test.val_test)
