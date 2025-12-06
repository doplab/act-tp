# Question 3
def K_nearest_neighbor(start, point_set, K):
    k_nearest_nei = []

    for j in range(K):  # A chaque itération, on applique l'algorithme du nearest neighbor mais sur un ensemble de points réduit
        point, distance = nearest_neighbor(start, point_set)
        k_nearest_nei.append((point[0], point[1], distance))
        point_set.remove(point)  # On retire de l'ensemble de points le voisin le plus proche, de cette manière, à chaque itération,
        # le voisin le plus proche sera de plus en plus éloigné.

    return k_nearest_nei