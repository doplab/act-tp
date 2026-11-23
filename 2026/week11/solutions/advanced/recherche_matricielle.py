# Version 1 : parcours de toutes les cases
def recherche_matricielle(matrice, e):
    for ligne in range(len(matrice)):
        for colonne in range(len(matrice[ligne])):
            if matrice[ligne][colonne] == e:
                return (ligne, colonne)
    return (-1, -1)

# Version 2 : recherche binaire dans chaque ligne
def recherche_matricielle(matrice, e):
    for ligne in range(len(matrice)):
        low = 0
        high = len(matrice[ligne]) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrice[ligne][mid] == e:
                return (ligne, mid)
            elif matrice[ligne][mid] < e:
                low = mid + 1
            else:
                high = mid - 1
    return (-1, -1)

if __name__ == '__main__':
    m = [[1,2,3,4],[4,5,7,8],[5,6,8,10],[6,7,9,11]]
    e = 61
    print(recherche_matricielle(m, e))
