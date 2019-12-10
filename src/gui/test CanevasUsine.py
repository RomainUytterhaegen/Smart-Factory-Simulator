from CanevasUsine import CanvasUsine, Tk, Frame
from Save import importer

cartet = importer("../cartet.json")
cartet.ajout_tache_atelier(0, 10)


class Test(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        window.title("Changement de couleur")
        self.pack()

        self.canvas = CanvasUsine(self, False, nlignes=20, ncolones=20, highlightthickness="4", highlightcolor='black',
                                  highlightbackground="black")
        self.canvas.pack()
        # a =self.canvas.after(200, self.canvas.carte.tour_simulation)
        self.etat = True
        # c = self.canvas.after(500, self.canvas.chargement, self.canvas.carte)

    def boucle_chargement(self):
        if self.etat:
            print("Position Robot:", self.canvas.carte.liste_robot[0].pos)
            self.canvas.after(10, self.canvas.carte.tour_simulation)
            self.canvas.after(120, self.canvas.chargement(self.canvas.carte))
            self.canvas.after(150, self.boucle_chargement)

    def toggle_etat(self):
        self.etat = not self.etat

    def test_fin(self):
        if self.etat:
            if self.canvas.carte.liste_robot[0].pos in \
                    self.canvas.carte.get_voisins(self.canvas.carte.liste_borne[0].pos1):
                self.toggle_etat()
                self.canvas.after(130, self.canvas.chargement(self.canvas.carte))
            else:
                self.canvas.after(10, self.test_fin)


if __name__ == '__main__':

    fenetre = Tk()
    usine = Test(window=fenetre)
    usine.canvas.chargement(cartet)
    print(cartet.get_pos_obstacles())
    usine.boucle_chargement()
    usine.after(10, usine.test_fin)
    # usine.after(5000, usine.toggle_etat)
    usine.after(500, lambda: print("Position Robot:", usine.canvas.carte.liste_robot[0].pos))
    usine.after(500, lambda: print("Position Robot cartet:", cartet.liste_robot[0].pos))
    usine.after(600, lambda: usine.canvas.chargement(cartet))
    usine.mainloop()
