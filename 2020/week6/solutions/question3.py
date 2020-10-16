def recherche_lineaire(L,e):
    for i in L:
        #Solution
        if i == e:
            return L.index(i) #L'algorithme prend fin aussi tôt que la valeur recherchée est trouvée.
    return -1 # Si la valeur n'a pas été trouvée, la fonction retourne -1
    
L = [1231321,3213125,3284016,4729273,5492710]
e = 3284016
recherche_lineaire(L,e)

