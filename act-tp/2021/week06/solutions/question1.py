#Définition de la fonction
def recherche_sequentielle(liste, x):
    for index in range(len(liste)):  # i représente l'index
        if liste[index] == x:
            print("X est présent dans la liste à l'index :", index)
            return index

    print("X n'est pas présent dans la liste")
    return -1

# Déclaration de la liste et de la variable x
L = [3, 55, 6, 8, 3, 5, 56, 33, 6, 5, 3, 2, 99, 53, 532, 75, 21, 963, 100, 445, 56, 45, 12, 56, 24]
e = 100

# Exécution de l'algorithme
resultat = recherche_sequentielle(L,e)
print(resultat)
