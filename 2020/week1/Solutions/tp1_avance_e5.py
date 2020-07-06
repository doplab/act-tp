# Exercice 17
liste_nombre = [[2, 3, 4], [1], [2, 7]]

nouvelle_liste = '/'.join([''.join([str(x) for x in l]) for l in liste_nombre])
print(nouvelle_liste)
