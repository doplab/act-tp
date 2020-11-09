#Question 2
#WARNING : Veillez ajouter le code de la question 1 au code ci-dessous pour que cela fonctionne.
#Librairie qui permettent de visualiser le résultat (pas nécessaire à la résolution du problème)
import matplotlib.pyplot as plt
import numpy as np

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

a = np.array([(1,2), (5,6), (7,8), (2,5), (9,1)])#List de points
b = (3,4)#Point de départ

point, distance = nearest_neighbor(b,a)
#Devrait output [2,5]

print("Le voisin le plus proche est ", point, " avec une distance de ", distance)

#Vous ne devez pas comprendre ce bout de code, il vous permet de visualiser le résultat
#Le point de départ apparait en orange, le voisin le plus proche en rouge
plt.scatter(a[:,0],a[:,1])
plt.scatter(b[0], b[1], color = 'orange')
plt.scatter(point[0], point[1], color = 'green')
