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