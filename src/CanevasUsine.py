from tkinter import *
from sys import stderr
from Formulaire import Formulaire
from Carte import Carte


class CanvasUsine(Canvas):
    selected = None
    last_xy = None

    def __init__(self, master=None, construct=False, **kwargs):

        self.taille_case = 20
        self.construct = construct

        try:
            self.nblignes = kwargs['nlignes']
            self.nbcolones = kwargs['ncolones']
        except KeyError:
            print("nblignes ou nbcolones a été mal défini lors de l'appel de Canevas Usine", file=stderr)
            self.nblignes = 20
            self.nbcolones = 20

        if 'carte' in kwargs.keys():
            self.carte = kwargs["carte"]
        else:
            self.carte = Carte("Default", self.nbcolones, self.nblignes)

        self.height = self.nblignes * self.taille_case
        self.width = self.nbcolones * self.taille_case + 100 * self.construct

        kwargs = {k: v for k, v in kwargs.items() if k not in ('nlignes', 'ncolones')}

        kwargs['height'] = self.height
        kwargs['width'] = self.width

        Canvas.__init__(self, master=master, **kwargs)

        if self.construct:
            # robots
            self.create_text(50, 15, text="ROBOT", )
            self.create_oval(40, 30, 40 + self.taille_case, 30 + self.taille_case,
                             activefill="#b9de16", fill="yellow",
                             tags=('copy_and_drop', 'robot_spawn'))

            # bornes
            self.create_text(50, 80, text="BORNE")
            self.create_rectangle(40, 95, 40 + self.taille_case, 95 + self.taille_case,
                                  activefill="#b9de16", fill="orange",
                                  tags=('copy_and_drop', 'borne_spawn'))

            # ateliers
            self.create_text(50, 140, text="ATELIER")
            self.create_rectangle(40, 155, 40 + self.taille_case, 155 + self.taille_case, activefill="#b9de16",
                                  fill="grey", tags=('copy_and_drop', 'atelier_spawn'))
            # obstacle
            self.create_text(50, 195, text="OBSTACLE")
            self.create_rectangle(40, 210, 40 + self.taille_case, 210 + self.taille_case, activefill="#b9de16",
                                  fill="black", tags=('copy_and_drop', 'obstacle_spawn'))

            # sep
            self.create_line(100 * self.construct, 0, 100 * self.construct, self.winfo_reqheight(), fill="black")

            self.bind_item()

        self._create_grid()

    def bind_item(self):
        self.tag_bind('copy_and_drop', "<ButtonPress-1>", self.on_item_click_copy)
        self.tag_bind('copy_and_drop', "<Button1-Motion>", lambda e: self._move_selected(e.x, e.y))
        self.tag_bind('copy_and_drop', "<ButtonRelease-1>", lambda e: self._move_selected(e.x, e.y, 0, True))

        self.tag_bind('resizeable', "<ButtonPress-3>", self.on_item_click)
        #  self.tag_bind('resizeable', "<Button3-Motion>", lambda e: self._resize_item(e.x, e.y))
        self.tag_bind('resizeable', "<ButtonRelease-3>", lambda e: self._resize_item(e.x, e.y, True))

        self.tag_bind('movable', "<ButtonPress-1>", self.on_item_click)
        self.tag_bind('movable', "<Button1-Motion>", lambda e: self._move_item(e.x, e.y))
        self.tag_bind('movable', "<ButtonRelease-1>", lambda e: self._move_item(e.x, e.y, 0, True))
        self.master.master.bind("<KeyRelease-Delete>", lambda e: self._suppr_current())

    def chargement(self, carte: Carte):
        self.carte = carte
        for atelier in self.carte.liste_atelier:
            x1, y1 = [i * self.taille_case for i in atelier.pos1]
            x2, y2 = [i * self.taille_case for i in atelier.pos2]
            self.create_rectangle(x1 + 100 * self.construct, y1, x2 + 100 * self.construct + self.taille_case,
                                  y2 + self.taille_case, tags=('movable', 'resizeable', 'atelier'), fill='gray')
        for borne in self.carte.liste_borne:
            x, y = [i * self.taille_case for i in borne.pos1]
            self.create_rectangle(x + 100 * self.construct, y, x + self.taille_case + 100 * self.construct,
                                  y+self.taille_case, tags=('movable', 'base'), fill='orange')
        for obstacle in self.carte.liste_obstacle:
            x1, y1 = [i * self.taille_case for i in obstacle.pos1]
            x2, y2 = [i * self.taille_case for i in obstacle.pos2]
            self.create_rectangle(x1 + 100 * self.construct, y1, x2 + 100 * self.construct + self.taille_case,
                                  y2 + self.taille_case, tags=('movable', 'resizeable', 'obstacle'), fill='black')
        self.delete('robot')
        for rob in self.carte.liste_robot:
            x, y = [i * self.taille_case for i in rob.pos]
            self.create_oval(x + 100 * self.construct, y, x + self.taille_case + 100 * self.construct,
                             y+self.taille_case, tags=('movable', 'robot'), fill='yellow')

    def on_item_click(self, event):
        self.last_xy = event.x, event.y

    def on_item_click_copy(self, event):
        self.on_item_click(event)
        self._copy_curent()

    def _copy_curent(self):
        iid = self.find_withtag('current')
        self.selected = self._copy_item(iid)

    def _copy_item(self, iid):
        # type_ = self.type(iid)
        # assert type_ == 'oval'
        coords = self.coords(iid)

        kwds = self.itemconfigure(iid)
        bak_tags = kwds['tags'][-1].split()
        kwds = {k: v[-1] for k, v in kwds.items() if k != 'tags'}

        if 'robot_spawn' in bak_tags:
            kwds['tags'] = 'movable robot'
        elif 'atelier_spawn' in bak_tags:
            kwds['tags'] = 'movable resizeable atelier'
        elif 'borne_spawn' in bak_tags:
            kwds['tags'] = 'movable base'
        elif 'obstacle_spawn' in bak_tags:
            kwds['tags'] = 'movable resizeable base'
        else:
            print("Erreur de tags :", bak_tags, file=stderr)

        if self.type(iid) == 'oval':
            return self.create_oval(*coords, **kwds)
        elif self.type(iid) == 'rectangle':
            return self.create_rectangle(*coords, **kwds)

    def _create_grid(self):
        for i in range(100 * self.construct + self.taille_case, self.width, self.taille_case):
            self.create_line(i, 0, i, self.height, fill="grey")
        self.create_line(self.width, 0, self.width, self.height, fill="black")

        for i in range(self.taille_case, self.height, self.taille_case):
            self.create_line(100 * self.construct, i, self.width, i, fill="grey")
        self.create_line(100 * self.construct, self.height, self.width, self.height, fill="black")

    def _create_robot(self):
        """
        action à effectuer à la création d'un robot
        Affiche une fenêtre de saisie des données
        :return:
        """
        donnees = {
            "Assemblage": (BooleanVar, "Oui", "Non"),
            "Transport": (BooleanVar, "Oui", "Non"),
            "Vitesse": (IntVar, 1, 2, 3, 4, 5)
        }

        top = Toplevel(self.master)
        top.transient(self.master)
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        topup = Formulaire(top, donnees, bg='#faf7f2')

        topup.grid(row=0, column=0, sticky='new')

        self.after(1000, self._verif_fin_formulaire, topup)

        top.mainloop()

    def _magnetisme(self, pos: tuple):
        """
        Algorithme trouvant l'objectif le plus proche
        :param pos: tuple (x, y) de départ
       """
        x, y = pos

        for i in range(self.taille_case):
            if (x - i) % self.taille_case == 0:
                x -= i
                break
            if (x + i) % self.taille_case == 0:
                x += i
                break

        for i in range(self.taille_case):
            if (y - i) % self.taille_case == 0:
                y -= i
                break
            if (y + i) % self.taille_case == 0:
                y += i
                break

        return x, y

    def _move_item(self, ex1, ey1, mini=5, magnetisme=False):

        if abs(self.last_xy[0] - ex1 + self.last_xy[1] - ey1) > mini:
            coords = list(self.coords('current'))
            x0 = coords[0] + ex1 - self.last_xy[0]
            x1 = coords[2] + ex1 - self.last_xy[0]
            y0 = coords[1] + ey1 - self.last_xy[1]
            y1 = coords[3] + ey1 - self.last_xy[1]

            if magnetisme:
                x0, y0 = self._magnetisme((x0, y0))
                x1, y1 = self._magnetisme((x1, y1))

            self.coords('current', x0, y0, x1, y1)
            self.last_xy = ex1, ey1
            self._verif_in_usine()

    def _move_selected(self, x1, y1, min_pixels=1, magnetisme=False):
        x0, y0 = self.last_xy
        dx, dy = x1 - x0, y1 - y0
        if abs(dx) > min_pixels or abs(dy) > min_pixels:
            if magnetisme:
                if 'robot' in self.gettags(self.selected):
                    self._create_robot()
                pass
                #  rajouter le mgnétisme ici?
            self.move(self.selected, dx, dy)
            self.last_xy = x1, y1

    def _resize_item(self, xe, ye, magnetisme=False):
        x0, y0, x1, y1 = self.coords('current')
        x1 += (xe - self.last_xy[0])
        y1 += (ye - self.last_xy[1])
        diffx = x1 - x0
        diffy = y1 - y0

        if magnetisme:
            x0, y0 = self._magnetisme((x0, y0))
            x1 = x0 + diffx
            y1 = y0 + diffy
            x1, y1 = self._magnetisme((x1, y1))
        if diffx >= self.taille_case-5 and diffy >= self.taille_case-5:
            self.coords('current', x0, y0, x1, y1)

    def _suppr_current(self):
        if 'movable' in self.gettags('current'):
            self.delete('current')

    def sync_drag_and_drop(self):
        """
        Fonction qui ajoute les objets créé via d&d dans la carte
        (Ou alors faire ça lors de la copîe)
        :return:
        """
        pass

    @staticmethod
    def test_coucou():
        print("coucou")

    def _verif_in_usine(self):
        """
        Verification des coordonées à droite de la ligne et dans le canvas

        """
        lx, ly1, ly2 = 100 * self.construct, 0, self.winfo_height()
        x0, y0, x1, y1 = list(self.coords('current'))
        largeur = x1 - x0 if x1 - x0 < self.width else self.width
        hauteur = y1 - y0 if y1 - y0 < self.height else self.height

        if x0 < lx and 'movable' in self.gettags('current'):
            x0 = lx
            x1 = x0 + largeur

        elif x1 > self.width and 'movable' in self.gettags('current'):
            x1 = self.width
            x0 = x1 - largeur

        if y0 < 0 and 'movable' in self.gettags('current'):
            y0 = 0
            y1 = y0 + hauteur
        elif y1 > self.height and 'movable' in self.gettags('current'):
            y1 = self.height
            y0 = y1 - hauteur

        self.coords('current', x0, y0, x1, y1)

    def _verif_fin_formulaire(self, form: Formulaire):
        if not form.fini:
            self.after(1000, self._verif_fin_formulaire, form)
        else:
            dic = form.retour
            self.carte.ajouter_robot(dic["Transport"], dic["Assemblage"], (0, 0), dic["Vitesse"])
            form.master.destroy()
            print(self.carte.liste_robot[0].pos, )





class Test(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)
        window.title("Changement de couleur")
        self.pack()

        self.canvas = CanvasUsine(self, True, nlignes=20, ncolones=20, highlightthickness="4", highlightcolor='black',
                                  highlightbackground="black")
        self.canvas.pack()


if __name__ == '__main__':
    root = Tk()
    test = Test(root)
    test.mainloop()
