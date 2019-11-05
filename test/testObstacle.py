from ...src.Obstacle import Obstacle


obst1 = Obstacle(00, (2, 1), (4, 2))
print("ID : ", obst1.getId())
print("Pos 1 :", obst1.getPos1())
print("Pos 2 : ", obst1.getPos2())
print("Hauteur : ", obst1.getHeight())
print("Largeur : ", obst1.getWidth())
