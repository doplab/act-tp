import random


def inside(point):  # Point est défini sous la forme d'un tuple
    # Cette fonction permet de vérifier si un point se trouve à l'intérieur du cercle
    if (point[0] ** 2 + point[1] ** 2) < 1:
        return 1

    else:
        return 0


def app():
    count = 0  # On initialise le nombre de points dans le cercle
    for i in range(10000):
        temp1 = random.random()  # Génère la première coordonnée
        temp2 = random.random()  # Génère la deuxième coordonnée
        temp = [temp1, temp2]  # Crée le point

        if (inside(temp)) :
            return temp # Retourne le point trouvé.


print("Voilà un point dans un cercle unitaire  : {}".format(app()))