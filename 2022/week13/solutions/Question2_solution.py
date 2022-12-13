from Exercice1_solution import calculate_distance
# Question 2
def nearest_neighbor(start, point_set):  # start correspond au point de départ, point_set correspond
    # à l'ensemble des points
    nearest_nei = None
    min_distance = None
    nearest_nei = None
    for i in range(len(point_set)):  # on parcourt tous les points de l'ensemble
        if i == 0:
            # La distance minimale n'étant pas définie, on doit l'initialiser à la première itération, c'est ce qu'on
            # fait ici
            min_distance = calculate_distance(start, point_set[0])
            nearest_nei = point_set[0]

        distance = calculate_distance(start, point_set[i])
        if distance < min_distance:
            min_distance = distance
            nearest_nei = point_set[i]

            # Cette partie du code détermine si le point actuellement considéré, est plus proche du point de départ que les points
        # parcourus jusqu'ici. Si c'est le cas, on redéfinit la distance minimale et on "enregistre" les coordonnées du point

    return nearest_nei, min_distance


if __name__ == '__main__':
    a = [(2, 3), (5, 6), (1, 4), (2, 4), (3, 5)]  # Liste de points
    b = (4, 4)  # Point de départ

    point, distance = nearest_neighbor(b, a)
    print(f'{point}, {distance}')
    # Devrait retourner (3, 5), 1.4142135623730951