def recherche_matricielle(m,l):
    #complètez ici
    for i in range(len(m)): # "Pour chaque ligne de la matrice" ou "Pour chaque liste de la liste"
        for j in range(len(m[i])): # "Pour chaque colonne de la matrice" ou "Pour chaque élément de la liste"
            if m[i][j] == l:
                return (i,j)#
    return (-1,-1)

m=[[1,2,3,4],[4,5,7,8],[5,6,8,10],[6,7,9,11]]
l=7
recherche_matricielle(m,l)