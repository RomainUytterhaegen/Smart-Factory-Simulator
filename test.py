# Chargement du module tkinter
from tkinter import * # pour Python2 se serait Tkinter

# Construction de la fenêtre principale «root»
root = Tk()
root.title('Simple exemple')

# Configuration du gestionnaire de grille
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Construction d'un simple bouton
qb = Button(root, text='Quitter', command=root.quit)

# Placement du bouton dans «root»
qb.grid(row=0, column=0, sticky="nsew")

# Lancement de la «boucle principale»
root.mainloop()
