def recherche_sequentielle(L,e):
    for elem in L:
        #Solution
        if elem == e:
            return L.index(elem) #L'algorithme prend fin aussitot que la valeur recherchée est trouvée.
    return -1 # Si la valeur n'a pas été trouvée, la fonction retourne -1

L = [123,321,328,472,549]
e = 328
resultat = recherche_sequentielle(L,e)
print(resultat)
