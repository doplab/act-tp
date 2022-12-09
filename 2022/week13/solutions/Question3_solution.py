#Question 3

def K_nearest_neighbor(start,point_set, K):
    temp = point_set #crée une copie de notre ensemble de points
    print(temp)
    k_nearest_nei = []
    
    for j in range(K): #A chaque itération on applique l'algorithme du nearest neighbour mais sur un ensemble de points réduit
        point, distance = nearest_neighbor(start,temp) 
        point.append(distance)
        k_nearest_nei.append(point)
        temp.remove(point) #On retire de l'ensemble de points le voisin le plus proche, de cette manière, à chaque itération,
        #le voisin le plus proche sera de plus en plus éloigné.
    
    return k_nearest_nei
