from tkinter import *
from Formulaire import Formulaire
from CanevasUsine import CanvasUsine, Carte


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
        self.boutons_haut.columnconfigure(5, weight=1)
        self.boutons_haut.columnconfigure(6, weight=1)
        self.boutons_haut.columnconfigure(7, weight=1)
        self.boutons_haut.rowconfigure(0, weight=1)

        self.boutons_haut.grid(row=0, column=0, sticky='news')

        # déclaration du contenu
        self.contenu = Frame(self, bg='#faf7f2')
        self.contenu.rowconfigure(0, weight=2)
        self.contenu.rowconfigure(1, weight=1)
        self.contenu.columnconfigure(0, weight=1)
        self.contenu.grid(row=1, column=0, sticky='news')

        self.message_textmode = Message(self.contenu, text=self.terminal_text(), width=300000, justify='left',
                                        highlightcolor='blue')
        self.message_textmode.grid(row=1, column=0, padx=20, pady=20, sticky='news')

        # Ajout des méthodes
        self.bouton_play = Button(self.boutons_haut, text="Lancer", command=self.lancer)
        self.bouton_pause = Button(self.boutons_haut, text="Pause", command=self.pauser)
        self.bouton_reinit = Button(self.boutons_haut, text="Reinitialiser", command=self.reinitialiser)
        self.bouton_modifier_robot = Button(self.boutons_haut, text="Modifier les robots", command=self.modifier_robot)
        self.bouton_voir_ateliers = Button(self.boutons_haut, text="Voir les ateliers",
                                           command=self.voir_ateliers)
        self.bouton_modifier_usine = Button(self.boutons_haut, text="Modifier l'usine", command=self.modifier_usine)
        self.bouton_mode_visuel = Button(self.boutons_haut, text="Passer en Mode visuel", command=self.mode_visuel)
        self.bouton_mode_text = Button(self.boutons_haut, text="Passer en Mode texte", command=self.mode_text)

        # pack des boutons
        self.bouton_play.grid(row=0, column=0, padx=2, pady=2, sticky='news')
        self.bouton_pause.grid(row=0, column=1, padx=2, pady=2, sticky='news')
        self.bouton_reinit.grid(row=0, column=2, padx=2, pady=2, sticky='news')
        self.bouton_modifier_robot.grid(row=0, column=3, padx=2, pady=2, sticky='news')
        self.bouton_voir_ateliers.grid(row=0, column=4, padx=2, pady=2, sticky='news')
        self.bouton_modifier_usine.grid(row=0, column=5, padx=2, pady=2, sticky='news')
        self.bouton_mode_visuel.grid(row=0, column=6, padx=2, pady=2, sticky='news')
        self.bouton_mode_text.grid(row=0, column=7, padx=2, pady=2, sticky='news')

        self.carte = Carte("Carte 1", 20, 20)

        # contenu du contenu
        self.mode_visuel()

    def lancer(self):
        """
        Lance la simulation de l'usine
        :return:
        """
        self.mode_visuel()

    def pauser(self):
        """
        Pause la simulation de l'usine
        :return:
        """
        self.mode_visuel()

    def reinitialiser(self):
        """
        Réinitialise la simulation de l'usine
        :return:
        """
        self.mode_visuel()

    def popup(self, frame, *args, **kwargs):
        top = Toplevel(self.master)
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        topup = frame(top, *args, **kwargs)

        topup.grid(row=0, column=0, sticky='new')

    def com_ajout_robot(self):

        donnees = {
            "Assemblage": (BooleanVar, "Oui", "Non"),
            "Transport": (BooleanVar, "Oui", "Non"),
            "Vitesse": (IntVar, 1, 2, 3, 4, 5)
        }

        self.popup(Formulaire, donnees, bg='#faf7f2')

    def modifier_robot(self):
        """
        Permet d'afficher l'écran qui ajoute un robot à la simulation
        :return:
        """
        self.contenu.destroy()
        self.contenu = Frame(self, bg='#faf7f2')
        self.contenu.rowconfigure(0, weight=1)
        self.contenu.columnconfigure(0, weight=1)
        self.contenu.grid(row=1, column=0, sticky='news')

        self.contenu.bouton_ajouter_robot = Button(self.contenu, text="Ajouter un robot",
                                                   command=self.com_ajout_robot)
        self.contenu.bouton_ajouter_robot.grid(row=0, column=0, padx=20, pady=20, sticky='news')

    def voir_ateliers(self):
        """
        Permet de voir la liste des tâches en cours
        :return:
        """
        self.contenu_non_implemente()

    def modifier_usine(self):
        """
        Permet d'afficher l'écran qui permet de modifier l'usine
        :return:
        """
        self.contenu.destroy()

        self.contenu = Frame(self, bg='#faf7f2')
        self.contenu.rowconfigure(0, weight=2)
        self.contenu.rowconfigure(1, weight=1)
        self.contenu.columnconfigure(0, weight=1)
        self.contenu.grid(row=1, column=0, sticky='news')

        self.canvas_usine = CanvasUsine(self.contenu, True, nlignes=20, ncolones=20)
        self.canvas_usine.grid(row=0, column=0, padx=20, pady=20, sticky='news')

        self.message_textmode = Message(self.contenu, text=self.terminal_text(), width=300000, justify='left',
                                        highlightcolor='blue')
        self.message_textmode.grid(row=1, column=0, padx=20, pady=20, sticky='news')

    def mode_visuel(self):
        """
        Permet d'afficher l'ecran de simulation 2d
        :return:
        """
        self.contenu.destroy()

        self.contenu = Frame(self, bg='#faf7f2')
        self.contenu.rowconfigure(0, weight=2)
        self.contenu.rowconfigure(1, weight=1)
        self.contenu.columnconfigure(0, weight=1)
        self.contenu.grid(row=1, column=0, sticky='news')

        self.canvas_usine = CanvasUsine(self.contenu, nlignes=20, ncolones=20)
        self.canvas_usine.chargement(self.carte)
        self.canvas_usine.grid(row=0, column=0, padx=20, pady=20, sticky='news')

        self.message_textmode = Message(self.contenu, text=self.terminal_text(), width=300000, justify='left',
                                        highlightcolor='blue')
        self.message_textmode.grid(row=1, column=0, padx=20, pady=20, sticky='news')

    def mode_text(self):
        """
        Permet d'afficher l'écran du mode texte
        :return:
        """
        self.contenu.destroy()

        self.contenu = Frame(self, bg='#faf7f2')
        self.contenu.rowconfigure(0, weight=1)
        self.contenu.columnconfigure(0, weight=1)
        self.contenu.grid(row=1, column=0, sticky='news')

        self.message_textmode = Message(self.contenu, text=self.terminal_text(), width=300000, justify='left',
                                        highlightcolor='blue')
        self.message_textmode.grid(row=0, column=0, padx=20, pady=20, sticky='news')

    @staticmethod
    def terminal_text():
        """
        défini ce que l'encadré de texte affiche
        :return: str le contenu du mode text
        """
        msg = '>>Initialisation de l\'usine...\n'
        # todo réussir à aligner le texte à gauche
        return msg

    def contenu_non_implemente(self):
        """
        Affiche un label pour prévenir l'utilisateur
        :return:
        """
        self.contenu.destroy()

        self.contenu = Frame(self, bg='red')
        self.contenu.rowconfigure(0, weight=1)
        self.contenu.columnconfigure(0, weight=1)
        self.contenu.grid(row=1, column=0, sticky='news')

        self.contenu.label_non_implemente = Label(self.contenu, text="Le contenu n'est pas encore implémenté", bg='red')
        self.contenu.label_non_implemente.grid(row=0, column=0, padx=20, pady=20, sticky='news')


"""
def formulaire(objet, window, **kwargs):
    for s,v in kwargs:
        objet.label window
"""

if __name__ == '__main__':
    fenetre = Tk()
    usine = GuiUsine(window=fenetre)
    usine.mainloop()
