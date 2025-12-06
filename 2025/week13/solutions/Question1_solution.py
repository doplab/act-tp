import math #permet d'importer la librairie nécessaire au calcul de la racine carrée

def calculate_distance(point1,point2):
    #Cette fonction retourne la distance euclidienne entre 2 points
    return math.sqrt((point2[0]-point1[0])**2+(point2[1]-point1[1])**2)
