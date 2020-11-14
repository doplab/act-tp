#Question 3
#WARNING :Veillez ajouter les fonctions des questions 1 et 2 pour que le code ci-dessous fonctionne
#Librairie qui permettent de visualiser les données, pas nécessaire pour la résolution de l'exercice
import numpy as np
import matplotlib.pyplot as plt
import math

def K_nearest_neighbor(start,point_set, K):
    temp = point_set #crée une copie de notre ensemble de point
    k_nearest_nei = []
    
    for j in range(K):#A chaque itération on applique l'algorithme du nearest neighbor mais sur un ensemble de point réduit
        point, distance = nearest_neighbor(start,temp) 
        point.append(distance)
        k_nearest_nei.append(point)
        temp.remove(point)#On retire de l'ensemble de points le voisin le plus proche, de cette manière, à chaque itération,
        #le voisin le plus proche sera de plus en plus éloigné.
    
    return k_nearest_nei

a = [[1,2], [5,8], [7,8], [2,5], [9,1]]#Liste de points
b = (3,4)#Point de départ
K = 2

n = K_nearest_neighbor(b,a,K)
print(n)

#Vous n'avez pas besoin de comprendre ce bout de code, il permet de visualiser votre résultat
a = np.array([[1,2], [5,8], [7,8], [2,5], [9,1]])
plt.scatter(a[:,0],a[:,1])
plt.scatter(b[0], b[1], color = 'Orange')

for i in range(K):
    plt.scatter(n[i][0], n[i][1], color = 'green')
