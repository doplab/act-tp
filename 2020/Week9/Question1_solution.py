import math #permet d'importer la librarie nécessaire au calcul de la racine carrée

def calculate_distance(point1,point2):
    #Implémentez la formule de la distance euclidienne entre 2 points ici
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
