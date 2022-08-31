#Exercice 1
import matplotlib.pyplot as plt

#Question 1
import math #permet d'importer la library nécessaire au calcul de la racine carrée

def calculate_distance(point1,point2):
    #Implémentez la formule de la distance euclidienne entre 2 point ici
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

#Question 2
def nearest_neighbor(start, point_set):#start correspond au point de départ, point_set correspond à l'ensemble des points
    for i in range(len(point_set)):#on parcourt tout les point de l'ensemble
        
        if i == 0:
            min_distance = calculate_distance(start, point_set[0])
            nearest_nei = point_set[0]
            #La distance minimale n'étant pas définie, on doit l'initialiser à la première itération, c'est ce qu'on fait ici
            
        distance = calculate_distance(start, point_set[i])
        
        if distance < min_distance:            
            min_distance = calculate_distance(start, point_set[i])
            nearest_nei = point_set[i]   
            
        #Cette partie du code détermine si le point actuellement considéré, est plus proche du point de départ que les points 
        #parcouru jusqu'ici. Si c'est le cas, on redéfinit la distance minimale et "enregistre" les coordonées du point
        
    return nearest_nei, min_distance

point_set = [[2,3],[5,6],[1,4],[2,4],[3,5]]#L'ensemble de point (en bleu dans le graphe)
start = [4,4]#Point de départ(orange dans le graphe)

#Ne vous occupez pas de cette partie du code, elle permet de visualiser notre ensemble de point et le point de départ
plt.scatter([i[0] for i in point_set], [i[1] for i in point_set])
plt.scatter(start[0], start[1])

#Le code fonctionne-t-il ?
point, distance = nearest_neighbor(start, point_set)
print("Le point le plus proche est {0} avec une distance de {1}".format(point, distance))

#Question 3

def K_nearest_neighbor(start,point_set, K):
    temp = point_set #crée une copie de notre ensemble de point
    print(temp)
    k_nearest_nei = []
    
    for j in range(K):#A chaque itération on applique l'algorithme du nearest neighbour mais sur un ensemble de point réduit
        point, distance = nearest_neighbor(start,temp) 
        point.append(distance)
        k_nearest_nei.append(point)
        temp.remove(point)#On retire de l'ensemble de point le voisin le plus proche, de cette manière, à chaque itération,
        #le voisin le plus proche sera de plus en plus éloigné.
    
    return k_nearest_nei

print(K_nearest_neighbor(start, point_set, 2))
