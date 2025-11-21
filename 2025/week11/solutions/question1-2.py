def recherche_sequentielle(liste, e):
    if e in liste:
        # L'algorithme prend fin aussitôt que la valeur recherchée est trouvée.
        return liste.index(e)
    return -1  # Si la valeur n'est pas trouvée, retourne -1


# Solution alternative
def recherche_sequentielle(liste, e):
    try:
        # L'algorithme prend fin aussitôt que la valeur recherchée est trouvée.
        return liste.index(e)
    except ValueError:
        return -1


if __name__ == '__main__':
    L = [123, 321, 328, 472, 549, 328]
    e = 328
    resultat = recherche_sequentielle(L, e)
    print(resultat)  # Affiche 2
