import os
from Borne import Borne
from Atelier import Atelier
from Obstacle import Obstacle
from Robot import Robot
from Carte import Carte


class Save:

    #carte
    def importer(nomCarte):
        chemin = os.path.join(curr_dir , nomCarte)
        with open(chemin+'/taille.json' , 'r') as json_data:
            Taille = json.load(json_data)
            x = Taille["x"]
            y = Taille["y"] 
        
            Obstacle = array()
            with open(chemin+'/borne.json','r') as json_data:
                liste = json.load(json_data)
                for j in liste["Borne"]:
                    b = Borne(j["id"] , j["pos1"] , j["pos2"])
                    Obstacle.append(b)

            with open(chemin+'/atelier.json','r') as json_data:
                liste = json.load(json_data)
                for j in liste["Atelier"]:
                    b = Atelier(j["id"] , j["pos1"] , j["pos2"] , j["utilite"] , j["tache"])
                    Obstacle.append(b)

            with open(chemin+'/obstacle.json','r') as json_data:
                liste = json.load(json_data)
                for j in liste["Obstacle"]:
                    b = Obstacle(j["id"] , j["pos1"] ,j["pos2"])
                    Obstacle.append(b)

        carte = carte(nomCarte , x , y , Obstacle)
        return carte
        

    def enregistrer(carte , Robots):
        chemin = os.path.join(curr_dir)
        if !(os.exists(chemin+carte.nom)):
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
                b.append({ "id" : j.getid() , "pos1" : j.getPos1() , "pos2" : j.getPos2()})
                
            if type(j) is Atelier :
                a.append({ "id" : j.getid() , "pos1" : j.getPos1() , "pos2" : j.getPos2() , "utilite" : j.getUtilite() , "tache" : j.getTache()})

            else :
                o.append({ "id" : j.getid() , "pos1" : j.getPos1() , "pos2" : j.getPos2()})

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
        for j in robot:
            r.append({"id" : j.id , "transport" : j.transport , "assemblage" : j.assemblage , "pos" : j.pos , "vitesse" : j.vitesse})
        with open(chemin+"/Robot.json" , "w+") as json_data:
            robots = dict({"Robot" : r})
            json.dump(robots, json_data , indent=4)
        

    #Robot
    def importer(nomCarte): 
        chemin = os.path.join(curr_dir , nomCarte)
        robot = array()
            with open(chemin+'/Robot.json','r') as json_data:
                liste = json.load(json_data)
                for j in liste["Robot"]:
                    b = Robot(j["id"] , j["transport"] , j["assemblage"]  , j["pos"] , j["vitesse"])
                    robot.append(b)
        return robot
    