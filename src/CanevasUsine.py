from tkinter import *
from sys import stderr


class CanvasUsine(Canvas):
    selected = None
    last_xy = None

    def __init__(self, master=None, construct=False, **kwargs):
        
        self.taille_case = 20
        self.construct = construct

        self.height = kwargs['nlignes'] * self.taille_case
        self.width = kwargs['ncolones'] * self.taille_case + 100 * self.construct

        kwargs = {k: v for k, v in kwargs.items() if k not in ('nlignes', 'ncolones')}

        kwargs['height'] = self.height
        kwargs['width'] = self.width

        Canvas.__init__(self, master=master, **kwargs)

        # robots
        self.create_text(50, 15, text="ROBOT", )
        self.create_rectangle(10, 30, 90, 110, activefill="#b9de16", fill="yellow",
                              tags=('copy_and_drop', 'robot_spawn'))

        # bornes
        self.create_text(50, 125, text="BORNE")
        self.create_rectangle(10, 140, 90, 220, activefill="#b9de16", fill="orange",
                              tags=('copy_and_drop', 'borne_spawn'))

        # equipements
        self.create_text(50, 235, text="EQUIPEMENT")
        self.create_rectangle(10, 250, 90, 330, activefill="#b9de16", fill="grey",
                              tags=('copy_and_drop', 'equipement_spawn'))

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

    def _move_selected(self, x1, y1, min_pixels=1, magnetisme=False):
        x0, y0 = self.last_xy
        dx, dy = x1 - x0, y1 - y0
        if abs(dx) > min_pixels or abs(dy) > min_pixels:
            if magnetisme:
                pass
                #  rajouter le mgnétisme ici?
            self.move(self.selected, dx, dy)
            self.last_xy = x1, y1

    def _move_item(self, ex1, ey1, mini=5, magnetisme=False):

        if abs(self.last_xy[0] - ex1 + self.last_xy[1] - ey1) > mini:
            coords = list(self.coords('current'))
            x0 = coords[0] + ex1 - self.last_xy[0]
            x1 = coords[2] + ex1 - self.last_xy[0]
            y0 = coords[1] + ey1 - self.last_xy[1]
            y1 = coords[3] + ey1 - self.last_xy[1]

            if magnetisme:
                x0, y0 = self.magnetisme((x0, y0))
                x1, y1 = self.magnetisme((x1, y1))

            self.coords('current', x0, y0, x1, y1)
            self.last_xy = ex1, ey1
            self._verif_in_usine()

    def _resize_item(self, xe, ye, magnetisme=False):
        x0, y0, x1, y1 = self.coords('current')
        x1 += (xe - self.last_xy[0])
        y1 += (ye - self.last_xy[1])
        diffx = x1-x0
        diffy = y1-y0

        if magnetisme:
            x0, y0 = self.magnetisme((x0, y0))
            x1 = x0 + diffx
            y1 = y0 + diffy
            x1, y1 = self.magnetisme((x1, y1))

        self.coords('current', x0, y0, x1, y1)

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
            self._create_robot()
        elif 'equipement_spawn' in bak_tags:
            kwds['tags'] = 'movable resizeable equipement'
        elif 'borne_spawn' in bak_tags:
            kwds['tags'] = 'movable resizeable base'
        else:
            print(bak_tags, file=stderr)

        if self.type(iid) == 'oval':
            return self.create_oval(*coords, **kwds)
        elif self.type(iid) == 'rectangle':
            return self.create_rectangle(*coords, **kwds)

    def _verif_in_usine(self):
        """
        Verification des coordonées à droite de la ligne et dans le canvas

        """
        lx, ly1, ly2 = 100 * self.construct, 0, self.winfo_height()
        x0, y0, x1, y1 = list(self.coords('current'))
        largeur = x1-x0 if x1-x0 < self.width else self.width
        hauteur = y1-y0 if y1-y0 < self.height else self.height

        if x0 < lx and 'movable' in self.gettags('current'):
            x0 = lx
            x1 = x0 + largeur

        elif x1 > self.width and 'movable' in self.gettags('current'):
            x1 = self.width
            x0 = x1-largeur

        if y0 < 0 and 'movable' in self.gettags('current'):
            y0 = 0
            y1 = y0 + hauteur
        elif y1 > self.height and 'movable' in self.gettags('current'):
            y1 = self.height
            y0 = y1 - hauteur

        self.coords('current', x0, y0, x1, y1)

    def _create_robot(self):
        """
        action à effectuer à la création d'un robot
        Affiche une fenêtre de saisie des données
        :return:
        """
        top = Toplevel(self.master, bg="red")
        top_lab = Label(top, text="COUC0U")
        top_lab.pack()

    def enregistrer(self):
        """
        enregistre dans un fichier json le contenu de l'usine
        Ce contenu est composé de tous les block situé à droite de la ligne.
        :return:
        """
        pass

    def _create_grid(self):
        for i in range(100 * self.construct+self.taille_case, self.width, self.taille_case):
            self.create_line(i, 0, i, self.height, fill="grey")
        self.create_line(self.width, 0, self.width, self.height, fill="black")

        for i in range(self.taille_case, self.height, self.taille_case):
            self.create_line(100 * self.construct, i, self.width, i, fill="grey")
        self.create_line(100 * self.construct, self.height, self.width, self.height, fill="black")

    def _suppr_current(self):
        if 'movable' in self.gettags('current'):
            self.delete('current')

    def magnetisme(self, pos: tuple):
        """
        Algorithme trouvant l'objectif le plus proche
        :param pos: tuple (x, y) de départ
       """
        x, y = pos

        print("deb", x, y)

        for i in range(self.taille_case):
            if (x-i) % self.taille_case == 0:
                x -= i
                break
            if (x+i) % self.taille_case == 0:
                x += i
                break

        for i in range(self.taille_case):
            if (y-i) % self.taille_case == 0:
                y -= i
                break
            if (y+i) % self.taille_case == 0:
                y += i
                break

        print("res", x, y, "\n")

        return x, y


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
