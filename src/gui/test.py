# from Carte import Carte

# # Chargement du module tkinter
# from tkinter import * # pour Python2 se serait Tkinter
#
# # Construction de la fenêtre principale «root»
# root = Tk()
# root.title('Simple exemple')
#
# # Configuration du gestionnaire de grille
# root.rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)
#
# # Construction d'un simple bouton
# qb = Button(root, text='Quitter', command=root.quit)
#
# # Placement du bouton dans «root»
# qb.grid(row=0, column=0, sticky="nsew")
#
# # Lancement de la «boucle principale»
# root.mainloop()

# l = (3, 4)
#
# x, y = [i * 20 for i in l]
#
# print(x, y, l)

# cartet = Carte("Coucou", 20, 20)
# cartet.ajouter_robot(True, True, (1, 1), 1)
# cartet.ajouter_obstacle((1, 2), (2, 4))
# cartet.ajouter_obstacle((5, 6), (10, 11))
# cartet.ajouter_obstacle((3, 11), (4, 15))
# cartet.ajouter_obstacle((13, 13), (14, 16))
# cartet.ajouter_obstacle((11, 11), (16, 12))
# cartet.ajouter_borne((15, 15))
#
# d = cartet.__dict__
# print(cartet.__dict__)
# c2 = Carte(" ", 10, 10)
# c2.__dict__ = d
# print(c2.__dict__)

