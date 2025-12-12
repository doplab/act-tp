import random


def inside(point):  # Point est défini sous la forme d'un tuple
    # Cette fonction permet de vérifier si un point se trouve à l'intérieur du cercle
    return (point[0] ** 2 + point[1] ** 2) <= 1


def app():
    while True:
        x = random.random()  # Génère la première coordonnée
        y = random.random()  # Génère la deuxième coordonnée
        p = (x, y)  # Crée le point

        if inside(p):
            return p  # Retourne le point trouvé.


print("Voilà un point dans un cercle unitaire  : {}".format(app()))
