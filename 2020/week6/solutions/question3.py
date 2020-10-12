def recherche_lineaire(L,e):
    for i in L:
        #Solution
        if i == e:
            return L.index(i)
    return -1
    
L = [1231321,3213125,3284016,4729273,5492710]
e = 3284016
recherche_lineaire(L,e)

%%time
print(recherche_lineaire(L,e))