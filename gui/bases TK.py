from tkinter import *


class GuiUsine(Frame):
    def __init__(self, window):
        Frame.__init__(self, window, bg='white')
        window.title('Simulation Usine')

        # responsive de self
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)

        self.grid(column=0, row=0, sticky="nsew")
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        # déclaration des grilles des boutons
        self.boutons_haut = Frame(self, bg='#faf7f2')
        self.boutons_haut.columnconfigure(0, weight=1)
        self.boutons_haut.columnconfigure(1, weight=1)
        self.boutons_haut.columnconfigure(2, weight=1)
        self.boutons_haut.columnconfigure(3, weight=1)
        self.boutons_haut.columnconfigure(4, weight=1)
        # self.boutons_haut.columnconfigure(5, weight=1)
        self.boutons_haut.columnconfigure(6, weight=1)
        self.boutons_haut.columnconfigure(7, weight=1)
        self.boutons_haut.rowconfigure(0, weight=1)

        self.boutons_haut.grid(row=0, column=0, sticky='news')

        # Ajout des méthodes
        self.bouton_play = Button(self.boutons_haut, text="Lancer", command=self.lancer())
        self.bouton_pause = Button(self.boutons_haut, text="Pause", command=self.pauser())
        self.bouton_reinit = Button(self.boutons_haut, text="Reinitialiser", command=self.reinitialiser())
        self.bouton_modifier_robot = Button(self.boutons_haut, text="Modifier les robot", command=self.modifier_robot())
        self.bouton_modifier_taches = Button(self.boutons_haut, text="Modifier les tâches", command=self.modifier_taches())
        self.bouton_modifier_usine = Button(self.boutons_haut, text="Modifier l'usine", command=self.modifier_usine())
        self.bouton_mode_visuel = Button(self.boutons_haut, text="Passer en Mode visuel", command=self.mode_visuel())
        self.bouton_mode_text = Button(self.boutons_haut, text="Passer en Mode texte", command=self.mode_text())

        # pack des boutons
        self.bouton_play.grid(row=0, column=0, padx=2, pady=2, sticky='news')
        self.bouton_pause.grid(row=0, column=1, padx=2, pady=2, sticky='news')
        self.bouton_reinit.grid(row=0, column=2, padx=2, pady=2, sticky='news')
        self.bouton_modifier_robot.grid(row=0, column=3, padx=2, pady=2, sticky='news')
        self.bouton_modifier_taches.grid(row=0, column=4, padx=2, pady=2, sticky='news')
        self.bouton_modifier_usine.grid(row=0, column=5, padx=2, pady=2, sticky='news')
        self.bouton_mode_visuel.grid(row=0, column=6, padx=2, pady=2, sticky='news')
        self.bouton_mode_text.grid(row=0, column=7, padx=2, pady=2, sticky='news')

        self.contenu = Frame(self, bg='#faf7f2')
        self.contenu.rowconfigure(0, weight=2)
        self.contenu.rowconfigure(1, weight=1)
        self.contenu.columnconfigure(0, weight=1)
        self.contenu.grid(row=1, column=0, sticky='news')

        # contenu du contenu
        self.canvas_usine = Canvas(self.contenu)
        self.canvas_usine.grid(row=0, column=0, padx=20, pady=20, sticky='news')

        self.message_textmode = Message(self.contenu, text=self.terminal_text(), width=300000, justify='left', highlightcolor='blue')
        self.message_textmode.grid(row=1, column=0, padx=20, pady=20, sticky='news')

    def lancer(self):
        """
        Lance la simulation de l'usine
        :return:
        """
        pass

    def pauser(self):
        """
        Pause la simulation de l'usine
        :return:
        """
        pass

    def reinitialiser(self):
        """
        Réinitialise la simulation de l'usine
        :return:
        """
        pass

    def modifier_robot(self):
        """
        Permet d'afficher l'écran qui ajoute un robot à la simulation
        :return:
        """
        pass

    def modifier_taches(self):
        """
        Permet de voir la liste des tâches en cours
        :return:
        """
        pass

    def modifier_usine(self):
        """
        Permet d'afficher l'écran qui permet de modifier l'usine
        :return:
        """
        pass

    def mode_visuel(self):
        """
        Permet d'afficher l'ecran de simulation 2d
        :return:
        """
        print('yolo')
        self.contenu = Frame(self, bg='blue')
        self.canvas_usine = Canvas(self.contenu)
        self.canvas_usine.grid(row=0, column=0, padx=20, pady=20, sticky='news')

        self.message_textmode = Message(self.contenu, text=self.terminal_text(), width=300000, justify='left', highlightcolor='blue')
        self.message_textmode.grid(row=1, column=0, padx=20, pady=20, sticky='news')
        pass

    def mode_text(self):
        """
        Permet d'afficher l'écran du mode texte
        :return:
        """
        pass

    def terminal_text(self):
        """
        défini ce que l'encadré de texte affiche
        :return: str le contenu du mode text
        """
        msg = '>>Initialisation de l\'usine...\n'
        # todo réussir à aligner le texte à gauche
        return msg


if __name__ == '__main__':
    fenetre = Tk()
    usine = GuiUsine(window=fenetre)
    usine.mainloop()
