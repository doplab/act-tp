import math  # permet d'importer la librairie nécessaire au calcul de la racine carrée
import matplotlib.pyplot as plt


# Question 1
def calculate_distance(point1, point2):
    # Cette fonction retourne la distance euclidienne entre 2 points
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Question 2
def nearest_neighbor(start, point_set):  # start correspond au point de départ, point_set correspond
    # à l'ensemble des points
    min_distance = None
    nearest_nei = []
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


# Question 3
def K_nearest_neighbor(start, point_set, K):
    k_nearest_nei = []

    for j in range(
            K):  # À chaque itération, on applique l'algorithme du nearest neighbour mais sur un ensemble de points réduit
        point, distance = nearest_neighbor(start, point_set)
        k_nearest_nei.append((point[0], point[1], distance))
        point_set.remove(
            point)  # On retire de l'ensemble de points le voisin le plus proche, de cette manière, à chaque itération,
        # le voisin le plus proche sera de plus en plus éloigné.

    return k_nearest_nei


if __name__ == '__main__':
    a = [(2, 3), (5, 6), (1, 4), (2, 4), (3, 5)]  # Liste de points
    b = (4, 4)  # Point de départ

    point, distance = nearest_neighbor(b, a)
    print(f'{point}, {distance}')
    # Devrait retourner (3, 5), 1.4142135623730951

    # Ne vous occupez pas de cette partie du code, elle permet de visualiser notre ensemble de point et le point de départ
    plt.scatter([i[0] for i in a], [i[1] for i in a])
    plt.scatter(b[0], b[1])
    plt.show()

    print(K_nearest_neighbor(b, a, 2))
    print(a)
