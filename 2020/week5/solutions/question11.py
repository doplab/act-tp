def merge(partie_gauche, partie_droite):
    # créer la liste qui sera retournée à la fin
    liste_fusionnee = []

    # définir un compteur pour l'index de la liste de gauche
    compteur_gauche = 0
    # pareil pour la liste de droite
    compteur_droite = 0

    longueur_gauche = len(partie_gauche)
    longueur_droite = len(partie_droite)

    # continuer jusqu'à ce que l'un des index (ou les deux) atteigne l'une des longueurs (ou les deux)
    while compteur_gauche < longueur_gauche and compteur_droite < longueur_droite:
        # comparer les éléments actuels, ajouter le plus petit à la liste fusionnée
        # et augmenter le compteur de cette liste
        if partie_gauche[compteur_gauche] < partie_droite[compteur_droite]:
            liste_fusionnee.append(partie_gauche[compteur_gauche])
            compteur_gauche += 1
        else:
            liste_fusionnee.append(partie_droite[compteur_droite])
            compteur_droite += 1

    # s'il y a encore des éléments dans les listes, il faut les ajouter à la liste fusionnée
    liste_fusionnee += partie_gauche[compteur_gauche:longueur_gauche]
    liste_fusionnee += partie_droite[compteur_droite:longueur_droite]

    return liste_fusionnee  # retourner la liste fusionnée


def tri_fusion(l):
    # complèter la fonction
    longueur = len(l)  # calculer la longueur de la liste
    # s'il n'y a pas plus d'un élément, retourner la liste
    if longueur == 1 or longueur == 0:
        return l
    # sinon, diviser la liste en deux
    elif longueur > 1:
        # convertir la variable en nombre entier (l'index ne peut pas être un nombre à virgule)
        index_milieu = int(longueur / 2)
        # la partie gauche va du 1er élément à celui du milieu
        partie_gauche = l[0:index_milieu]
        # la partie droite va du milieu à la fin de la liste
        partie_droite = l[index_milieu:longueur]

        # appeler la fonction tri_fusion à nouveau sur la partie gauche (récursivité)
        partie_gauche_triee = tri_fusion(partie_gauche)
        # même chose pour la partie droite
        partie_droite_triee = tri_fusion(partie_droite)

        liste_fusionnee = merge(partie_gauche_triee, partie_droite_triee)  # enfin, joindre les 2 parties

        # retourner le résultat
        return liste_fusionnee


if __name__ == "__main__":
    l = [38, 27, 43, 3, 9, 82, 10]
    print(tri_fusion(l))