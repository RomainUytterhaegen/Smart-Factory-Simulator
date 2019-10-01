from tkinter import *
"""Premier exemple avec Tkinter.


On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.


"""
"""

# On importe Tkinter

from tkinter import *


# On crée une fenêtre, racine de notre interface

fenetre = Tk()


# On crée un label (ligne de texte) souhaitant la bienvenue

# Note : le premier paramètre passé au constructeur de Label est notre

# interface racine

champ_label = Label(fenetre, text="Coucou")


# On affiche le label dans la fenêtre

champ_label.pack()


var_texte = StringVar()

ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)

ligne_texte.pack()

var_case = IntVar()

case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)

case.pack()

var_choix = StringVar()


choix_rouge = Radiobutton(fenetre, text="Rouge", variable=var_choix, value="rouge")

choix_vert = Radiobutton(fenetre, text="Vert", variable=var_choix, value="vert")

choix_bleu = Radiobutton(fenetre, text="Bleu", variable=var_choix, value="bleu")


choix_rouge.pack()

choix_vert.pack()

choix_bleu.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()

class Interface(Frame):
    Notre fenêtre principale.

    Tous les widgets sont stockés comme attributs de cette fenêtre.

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)

        self.pack(fill=BOTH)

        self.nb_clic = 0

        # Création de nos widgets

        self.message = Label(self, text="Vous n'avez pas cliqué sur le bouton.")

        self.message.pack()

        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)

        self.bouton_quitter.pack(side="left")

        self.bouton_cliquer = Button(self, text="Cliquez ici", fg="red",

                                     command=self.cliquer)

        self.bouton_cliquer.pack(side="right")

    def cliquer(self):
        Il y a eu un clic sur le bouton.



        On change la valeur du label message.

        self.nb_clic += 1

        self.message["text"] = "Vous avez cliqué {} fois.".format(self.nb_clic)


fenetre = Tk()

interface = Interface(fenetre)


interface.mainloop()

interface.destroy()
"""


class GuiUsine(Frame):
    def __init__(self, fenetre):
        Frame.__init__(self, fenetre, width=1080, height=720)
        self.pack(fill=BOTH)

        # déclaration des boutons
        self.bouton_play = Button(self, text="Jouer", command=self.jouer())
        self.bouton_pause = Button(self, text="Pause", command=self.pauser())
        self.bouton_reinit = Button(self, text="Reinitialiser", command=self.reinitialiser())
        self.bouton_ajouter_robot = Button(self, text="Ajouter un robot", command=self.ajouter_robot())
        self.bouton_visualiser_taches = Button(self, text="Visualiser la liste des tâches",
                                               command=self.visualiser_taches())
        self.bouton_ajouter_taches = Button(self, text="Ajouter des Tâches", command=self.ajouter_taches())
        self.bouton_mode_text = Button(self, text="Passer en Mode texte", command=self.mode_text())
        self.bouton_modifier_usine = Button(self, text="Modifier l'usine", command=self.modifier_usine())

        # pack des boutons
        self.bouton_play.pack()
        self.bouton_pause.pack()
        self.bouton_reinit.pack()
        self.bouton_ajouter_robot.pack()
        self.bouton_visualiser_taches.pack()
        self.bouton_ajouter_taches.pack()
        self.bouton_mode_text.pack()
        self.bouton_modifier_usine.pack()

    def jouer(self):
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

    def ajouter_robot(self):
        """
        Permet d'afficher l'écran qui ajoute un robot à la simulation
        :return:
        """
        pass

    def visualiser_taches(self):
        """
        Permet de voir la liste des tâches en cours
        :return:
        """
        pass

    def ajouter_taches(self):
        """
        Permet d'afficher l'écran qui permet d'ajouter des tâches
        :return:
        """
        pass

    def modifier_usine(self):
        """
        Permet d'afficher l'écran qui permet de modifier l'usine
        :return:
        """
        pass

    def mode_text(self):
        """
        Permet d'afficher l'écran du mode texte
        :return:
        """
        pass


if __name__ == '__main__':
    fenetre = Tk()
    usine = GuiUsine(fenetre=fenetre)
    usine.mainloop()
