# Definition de la fonction ayant pour argument une liste et un nombre
def plus_proche_sequentielle(liste, nb):
    # Initialisation de la variable (-1 car les différence calculée après seront toujours positives)
    diff = -1
    resultat = None  # Initialisation de la variable pour le résultat

    # Complètez ici


if __name__ == '__main__':
    # Déclaration de la liste et de la variable e
    L = [16, 2, 25, 8, 12, 31, 2, 56, 58, 63]
    e = 50

    # Exécution de la fonction
    resultat = plus_proche_sequentielle(L, e)
    print(resultat)
