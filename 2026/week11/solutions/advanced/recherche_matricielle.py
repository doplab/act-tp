def recherche_matricielle(m,e):
    #complètez ici
    for ligne in range(len(m)): # "Pour chaque ligne de la matrice" ou "Pour chaque liste de la liste"
        for colonne in range(len(m[ligne])): # "Pour chaque colonne de la matrice" ou "Pour chaque élément de la liste"
            if m[ligne][colonne] == e:
                return (ligne,colonne)
    return (-1,-1)

if __name__ == '__main__':
    m=[[1,2,3,4],[4,5,7,8],[5,6,8,10],[6,7,9,11]]
    e=61
    print(recherche_matricielle(m,e))
