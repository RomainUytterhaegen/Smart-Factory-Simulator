from CanevasUsine import CanvasUsine, Tk, Frame
from Carte import Carte
from time import sleep

cartet = Carte("Coucou", 10, 10)
cartet.ajouter_robot(True, True, (1, 1), 1)
cartet.ajouter_obstacle((1, 2), (2 , 4))
cartet.ajouter_obstacle((5, 6), (10, 11))
#cartet.ajouter_borne()

class Test(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        window.title("Changement de couleur")
        self.pack()

        self.canvas = CanvasUsine(self, True, nlignes=20, ncolones=20, highlightthickness="4", highlightcolor='black',
                                  highlightbackground="black")
        self.canvas.pack()

        self.canvas.chargement(cartet)
        # a =self.canvas.after(200, self.canvas.carte.tour_simulation)
        b = self.canvas.after(100, self.canvas.test_coucou)
        self.etat = True
        # c = self.canvas.after(500, self.canvas.chargement, self.canvas.carte)

    def boucle_chargement(self):
        if self.etat:
            self.canvas.after(10, self.canvas.test_coucou)
            self.canvas.after(100, self.boucle_chargement)

    def toggle_etat(self):
        self.etat = not self.etat


if __name__ == '__main__':

    fenetre = Tk()
    usine = Test(window=fenetre)
    usine.boucle_chargement()
    usine.after(5000, usine.toggle_etat)
    usine.mainloop()