import math #permet d'importer la librairie nécessaire au calcul de la racine carrée

# Question 1
def calculate_distance(point1,point2):
    #Cette fonction retourne la distance euclidienne entre 2 points
    return math.sqrt((point2[0]-point1[0])**2+(point2[1]-point1[1])**2)

# Question 2
def nearest_neighbor(start, point_set):  # start correspond au point de départ, point_set correspond
    # à l'ensemble des points
    nearest_nei = None
    min_distance = calculate_distance(start, point_set[0]) # on initialise la distance minimale avec la valeur de la distance entre start et point_set[0]
    nearest_nei = point_set[0]  # on initialise le point le plus proche avec la valeur du premier point

    for i in range(len(point_set)):  # on parcourt tous les points de l'ensemble
        distance = calculate_distance(start, point_set[i])
        if distance < min_distance:
            min_distance = distance
            nearest_nei = point_set[i]

            # Cette partie du code détermine si le point actuellement considéré, est plus proche du point de départ que les points
        # parcourus jusqu'ici. Si c'est le cas, on redéfinit la distance minimale et on "enregistre" les coordonnées du point

    return nearest_nei, min_distance # ou (nearest_nei, min_distance)


if __name__ == '__main__':
    a = [(2, 3), (5, 6), (1, 4), (2, 4), (3, 5)]  # Liste de points
    b = (4, 4)  # Point de départ

    point, distance = nearest_neighbor(b, a)
    print(f'{point}, {distance}')
    # Devrait retourner (3, 5), 1.4142135623730951