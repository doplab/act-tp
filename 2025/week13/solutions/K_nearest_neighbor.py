import math #permet d'importer la librairie nécessaire au calcul de la racine carrée

# Question 1
def calculate_distance(point1,point2):
    #Cette fonction retourne la distance euclidienne entre 2 points
    return math.sqrt((point2[0]-point1[0])**2+(point2[1]-point1[1])**2)

# Question 2
def nearest_neighbor(start, point_set):  # start correspond au point de départ, point_set correspond
    # à l'ensemble des points
    if(len(point_set) == 0): 
        return None, None
    min_distance = calculate_distance(start, point_set[0]) # on initialise la distance minimale avec la valeur de la distance entre start et point_set[0]
    nearest_nei = point_set[0]  # on initialise le point le plus proche avec la valeur du premier point

    for i in range(len(point_set)):  # on parcourt tous les points de l'ensemble
        distance = calculate_distance(start, point_set[i])
        # Cette partie du code détermine si le point actuellement considéré, est plus proche du point de départ que les points précédents
        if distance < min_distance:
            min_distance = distance
            nearest_nei = point_set[i] # si c'est le cas, on redéfinit la distance minimale et on "enregistre" les coordonnées du point

    return nearest_nei, min_distance # ou (nearest_nei, min_distance)

# Question 3
def K_nearest_neighbor(start, point_set, K):
    k_nearest_nei = []

    for j in range(min(K,len(point_set))):  # A chaque itération, on applique l'algorithme du nearest neighbor mais sur un ensemble de points réduit
        point, distance = nearest_neighbor(start, point_set)
        k_nearest_nei.append((point, distance))
        if point is not None: # si K est plus grand que le nombre de points dans point_set, on évite une erreur en vérifiant que point n'est pas None
            point_set.remove(point)  # On supprime de l'ensemble de points le voisin le plus proche, de cette manière. A chaque itération, le voisin le plus proche sera de plus en plus éloigné.

    return k_nearest_nei

if __name__ == '__main__':
    a = [(2, 3), (5, 6), (1, 4), (2, 4), (3, 5)]  # Liste de points
    b = (4, 4)  # Point de départ

    k_nearest_neighbors = K_nearest_neighbor(b, a, 2)
    print(k_nearest_neighbors)
    # Devrait afficher [((3, 5), 1.4142135623730951), ((2, 4), 2.0)]
    for point, distance in k_nearest_neighbors:
        print(f'{point}, {distance}')
    # Devrait afficher (3, 5), 1.4142135623730951 et (2, 4), 2.0