from CanevasUsine import CanvasUsine, Tk, Frame
from Carte import Carte
from time import sleep

cartet = Carte("Coucou", 10, 10)
cartet.ajouter_robot(True, True, (1, 1), 1)
cartet.ajouter_obstacle((1, 2), (2 , 4))


class Test(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        window.title("Changement de couleur")
        self.pack()

        self.canvas = CanvasUsine(self, True, nlignes=20, ncolones=20, highlightthickness="4", highlightcolor='black',
                                  highlightbackground="black")
        self.canvas.pack()

        self.canvas.chargement(cartet)
        a =self.canvas.after(200, self.canvas.carte.tour_simulation)
        b = self.canvas.after(100, self.canvas.test_coucou)
        c = self.canvas.after(500, self.canvas.chargement, self.canvas.carte)



if __name__ == '__main__':

    fenetre = Tk()
    usine = Test(window=fenetre)
    fenetre.after(10, fenetre.bell)
    usine.mainloop()