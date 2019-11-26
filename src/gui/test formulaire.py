from tkinter import *
from Formulaire import Formulaire
from time import sleep


class Test(Frame):
    def __init__(self, window):
        Frame.__init__(self, window, bg='white')
        self.pack()

        self.dic = {}
        self.button = Button(self, text="Coucou", command=self.topeur)
        self.button.pack()
        print(self.dic)

    def topeur(self):
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

        dic = topup.retour
        print("c'est destrui")

        self.dic = dic




root = Tk()
test = Test(root)
test.mainloop()
