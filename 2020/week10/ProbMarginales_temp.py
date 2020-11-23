def produit_scalaire(vec, mat):
    # vec: liste de n elements
    # mat: liste de n sous-listes
    result = []
    for i in range(len(mat[0])): #iterer sur les colonnes de la matrice
        total = 0
        for j in range(len(vec)): # iterer sur les elements du vecteur et les lignes de la matrice
            total += vec[j] * mat[j][i]
        result.append(total)
    return result
            
def puissance_mat(mat, n):
    # P: liste de listes
    # n: integer
    new_mat = mat
    for i in range(n-1):
        dot_prod = [] # produit scalaire entre chaque ligne et la matrice complète
        ... # Partie à compléter
    return new_mat

def prob_marginales(mu_0, P, n):
    return ... # Partie à compléter
    
    
mu_0 = [0.3, 0.4, 0.3]
P = [[0.1, 0.2, 0.7],
    [0.9, 0.1, 0.],
    [0.1, 0.8, 0.1]]
n = 2 # puissance

print(prob_marginales(mu_0, P, n))