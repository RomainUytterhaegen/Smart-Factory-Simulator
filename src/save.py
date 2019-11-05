import os
from Borne import Borne
from Atelier import Atelier
from Obstacle import Obstacle
from Robot import Robot
from Carte import Carte


class Save:

   
    def importer(carte:Carte):
        """
        Transformation du contenue des fichiers json compris dans le dossier 'nomCarte' en objet carte
        avec la liste des obstacles remplies , la taille et son nom definie
        :parametre: une carte a remplir et deja enregistrer
        :return: un objet carte remplit
        """

        chemin = os.path.join(curr_dir , carte.nom)
        if (os.exists(chemin)):
            with open(chemin+'/taille.json' , 'r') as json_data:
                Taille = json.load(json_data)
                carte.x = Taille["x"]
                carte.y = Taille["y"] 
                Obstacle = array()

                with open(chemin+'/borne.json','r') as json_data:
                    liste = json.load(json_data)
                    for j in liste["Borne"]:
                        b = Borne(j["id"] , j["pos1"] , j["pos2"])
                        carte.listeObstacle.append(b)

                with open(chemin+'/atelier.json','r') as json_data:
                    liste = json.load(json_data)
                    for j in liste["Atelier"]:
                        b = Atelier(j["id"] , j["pos1"] , j["pos2"] , j["utilite"] , j["tache"])
                        carte.listeObstacle.append(b)

                with open(chemin+'/obstacle.json','r') as json_data:
                    liste = json.load(json_data)
                    for j in liste["Obstacle"]:
                        b = Obstacle(j["id"] , j["pos1"] ,j["pos2"])
                        carte.listeObstacle.append(b)

                with open(chemin+'/Robot.json','r') as json_data:
                    liste = json.load(json_data)
                    for j in liste["Robot"]:
                        b = Robot(j["id"] , j["transport"] , j["assemblage"]  , j["pos"] , j["vitesse"])
                        carte.listeRobot.append(b)
        
    
    def enregistrer(carte:Carte):
        """
        Transforme une carte et une liste de robot en fichier json
        Prend en paramètre une carte  et la liste des robot dans la carte
        :parametre: un objet carte 
        """

        chemin = os.path.join(curr_dir)
        if not(os.exists(chemin+carte.nom)):
            os.mkdir(os.path.join(curr_dir , nomCarte))
        chemin = os.path.join(curr_dir , nomCarte)
        o = []
        b = []
        a = []

        with open(chemin+'/taille.json' , 'w+') as json_data:
            Taille = {"x" : carte.x , "y" : carte.y}
            json.dump(Taille, json_data , indent=4)

        for j in carte.listeObstacle:
            if type(j) is Borne :
                b.append({ "id" : j.id , "pos1" : j.pos1 , "pos2" : j.pos2})
                
            if type(j) is Atelier :
                a.append({ "id" : j.id , "pos1" : j.pos1 , "pos2" : j.pos2 , "utilite" : j.utilite , "tache" : j.tache})

            else :
                o.append({ "id" : j.id , "pos1" : j.pos1 , "pos2" : j.pos2})

        with open(chemin+"/obstacle.json" , "w+") as json_data:
            obstacles = dict({"Obstacle" : o})
            json.dump(obstacles, json_data , indent=4)

        with open(chemin+"/borne.json" , "w+") as json_data:
            bornes = dict({"Borne" : b})
            json.dump(bornes, json_data , indent=4)

        with open(chemin+"/atelier.json" , "w+") as json_data:
            ateliers = dict({"Atelier" : a})
            json.dump(ateliers, json_data , indent=4)
        
        r = []
        for j in carte.listeRobot:
            r.append({"id" : j.id , "transport" : j.transport , "assemblage" : j.assemblage , "pos" : j.pos , "vitesse" : j.vitesse})
        with open(chemin+"/robot.json" , "w+") as json_data:
            robots = dict({"Robot" : r})
            json.dump(robots, json_data , indent=4)
        