from Carte import Carte
from Save import importer


class ControlleurTexte:

    def __init__(self, carte: Carte):
        self.carte = carte
        self.dic_command = {
            "HELP": lambda: f"Les commandes valides sont: {self.dic_command.keys()}",
            "AJOUT_ROBOT": lambda ass, pos, trans:  self.carte.ajouter_robot(ass, pos, trans)+"Le robot a été ajouté"
        }

    def lecture(self, command: str):
        command, *arg = command.split()
        command = command.upper()
        if arg:

            # Au pire faire une batterie de tests
            arg = arg[0].replace(";", ",").replace(" ", "")  # ''.join(arg).split(';')
            args=list()
            exec('args='+arg)
            args = list(args)

        try:
            if command in self.dic_command.keys():
                message_reussite = self.dic_command[command](*arg)
                return message_reussite
            else:
                return f"La commande {command} n'existe pas"
        except TypeError:
            return f"La commande {command} n'a pas reçu les bons arguments "


if __name__ == '__main__':
    c = importer("cartet.json")
    ct = ControlleurTexte(c)
    print(ct.lecture("Help"))
    print(ct.lecture("Ajout_robot True;(1,1);True"))
