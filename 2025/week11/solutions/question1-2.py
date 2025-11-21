def recherche_sequentielle(L,e):
    if e in L:
        return L.index(e) #L'algorithme prend fin aussitot que la valeur recherchée est trouvée.
    return -1 # Si la valeur n'est pas trouvée, retourne -1

# Solution alternative 
def recherche_sequentielle(L,e):
    try:
        return L.index(e) #L'algorithme prend fin aussitot que la valeur recherchée est trouvée.
    except ValueError:
        return -1

if __name__ == '__main__':
    L = [123,321,328,472,549,328]
    e = 328
    resultat = recherche_sequentielle(L,e)
    print(resultat) # Affiche 2
