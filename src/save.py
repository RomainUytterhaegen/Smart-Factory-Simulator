import json
from Borne import Borne
from Atelier import Atelier
from Obstacle import Obstacle
from Robot import Robot
from Ouvrier import Ouvrier
from Carte import Carte


class CarteEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


def exporter(carte: Carte):
    """

    :param carte:
    :return:
    """
    with open(f'{carte.nom}.json', 'w') as outfile:
        json.dump(carte, outfile, cls=CarteEncoder, indent=4)


def importer(chemin: str):
    """
    importe une Carte
    Produit une erreur si le fichier est inconnu ou n'est pas une carte
    :param chemin: Le chemin de la carte, fichier json inclus
    :return: Le premier objet carte du fichier chemin
    """
    with open(chemin, 'r') as infile:
        dico_carte = json.load(infile)

    for i in range(len(dico_carte['liste_obstacle'])):
        dico_carte['liste_obstacle'][i] = typifier(dico_carte['liste_obstacle'][i], Obstacle)

    for i in range(len(dico_carte['liste_robot'])):
        dico_carte['liste_robot'][i] = typifier(dico_carte['liste_robot'][i], Robot)

    for i in range(len(dico_carte['liste_atelier'])):
        dico_carte['liste_atelier'][i] = typifier(dico_carte['liste_atelier'][i], Atelier)

    for i in range(len(dico_carte['liste_borne'])):
        dico_carte['liste_borne'][i] = typifier(dico_carte['liste_borne'][i], Borne)

    for i in range(len(dico_carte['liste_ouvrier'])):
        dico_carte['liste_ouvrier'][i] = typifier(dico_carte['liste_ouvrier'][i], Ouvrier)

    return typifier(dico_carte, Carte)


def typifier(objet: dict, typer: type):
    """
    Création d'un objet à partir de ses attributs. Repose sur le fonctionnement très bas niveau de Python
    :param objet: __dict__ d'un objet
    :param typer: classe d'un objet
    :return: un Objet de type type et obj.__dict__ == objet
    """
    obj = typer.__new__(typer, "obj")
    obj.__dict__ = objet
    return obj

# class Save2:
#
#     def importer(self, carte: Carte):
#         """
#         Transformation du contenue des fichiers json compris dans le dossier 'nomCarte' en objet carte
#         avec la liste des obstacles remplies , la taille et son nom definie
#         :parametre: une carte a remplir et deja enregistrer
#         :return: un objet carte remplit
#         """
#
#         chemin = os.path.join(__file__, carte.nom)
#         if (os.path.exists(chemin)):
#             with open(chemin+'/taille.json' , 'r') as json_data:
#                 Taille = json.load(json_data)
#                 carte.x = Taille["x"]
#                 carte.y = Taille["y"]
#                 liste_obstacle = []
#
#                 with open(chemin+'/borne.json','r') as json_data:
#                     liste = json.load(json_data)
#                     for j in liste["Borne"]:
#                         b = Borne(j["id"] , j["pos1"] , j["pos2"])
#                         carte.liste_obstacle.append(b)
#
#                 with open(chemin+'/atelier.json','r') as json_data:
#                     liste = json.load(json_data)
#                     for j in liste["Atelier"]:
#                         b = Atelier(j["id"] , j["pos1"] , j["pos2"] , j["utilite"] , j["tache"])
#                         carte.liste_obstacle.append(b)
#
#                 with open(chemin+'/obstacle.json','r') as json_data:
#                     liste = json.load(json_data)
#                     for j in liste["Obstacle"]:
#                         b = Obstacle(j["id"] , j["pos1"] ,j["pos2"])
#                         carte.liste_obstacle.append(b)
#
#                 with open(chemin+'/Robot.json','r') as json_data:
#                     liste = json.load(json_data)
#                     for j in liste["Robot"]:
#                         b = Robot(j["id"] , j["transport"] , j["assemblage"]  , j["pos"] , j["vitesse"])
#                         carte.liste_robot.append(b)
#
#
#     def enregistrer(self,carte:Carte):
#         """
#         Transforme une carte et une liste de robot en fichier json
#         Prend en paramètre une carte  et la liste des robot dans la carte
#         :parametre: un objet carte
#         """
#
#         chemin = os.path.join(__file__)
#         if not(os.path.exists(chemin+carte.nom)):
#             os.mkdir(os.path.join(__file__ , carte.nom))
#         chemin = os.path.join(__file__ , carte.nom)
#         o = []
#         b = []
#         a = []
#
#         with open(chemin+'/taille.json' , 'w+') as json_data:
#             Taille = {"x" : carte.x , "y" : carte.y}
#             json.dump(Taille, json_data , indent=4)
#
#         for j in carte.listeObstacle:
#             if type(j) is Borne :
#                 b.append({ "id" : j.id , "pos1" : j.pos1 , "pos2" : j.pos2})
#
#             if type(j) is Atelier :
#                 a.append({ "id" : j.id , "pos1" : j.pos1 , "pos2" : j.pos2 ,
#                          "utilite" : j.utilite , "tache" : j.tache})
#
#             else :
#                 o.append({ "id" : j.id , "pos1" : j.pos1 , "pos2" : j.pos2})
#
#         with open(chemin+"/obstacle.json" , "w+") as json_data:
#             obstacles = dict({"Obstacle" : o})
#             json.dump(obstacles, json_data , indent=4)
#
#         with open(chemin+"/borne.json" , "w+") as json_data:
#             bornes = dict({"Borne" : b})
#             json.dump(bornes, json_data , indent=4)
#
#         with open(chemin+"/atelier.json" , "w+") as json_data:
#             ateliers = dict({"Atelier" : a})
#             json.dump(ateliers, json_data , indent=4)
#
#         r = []
#         for j in carte.listeRobot:
#             r.append({"id" : j.id , "transport" : j.transport , "assemblage" : j.assemblage ,
#                      "pos" : j.pos , "vitesse" : j.vitesse})
#         with open(chemin+"/robot.json" , "w+") as json_data:
#             robots = dict({"Robot" : r})
#             json.dump(robots, json_data , indent=4)


if __name__ == '__main__':
    cartet = Carte("cartet", 20, 20)
    cartet.ajouter_robot(True, True, (1, 1), 1)
    cartet.ajouter_obstacle((1, 2), (2, 4))
    cartet.ajouter_obstacle((5, 6), (10, 11))
    cartet.ajouter_obstacle((3, 11), (4, 15))
    cartet.ajouter_obstacle((13, 13), (14, 16))
    cartet.ajouter_obstacle((11, 11), (16, 12))
    cartet.ajouter_borne((15, 15))

    print(cartet.__dict__)
    exporter(cartet)
    # print(json.dumps(cartet, cls=CarteEncoder))
    c = importer("cartet.json")
    print(c.__dict__)
