#Definition de la fonction ayant pour argument une liste et un nombre
def plus_proche_sequentielle(liste,nb):
    diff = -1 #Initialisation de la variable ( -1 car les différences calculées après seront toujours positives)
    resultat = None #Initialisation de la variable pour le résultat

    #Solution
    for elem in liste:
        if diff == -1 or abs(elem-nb) < diff:
            diff = abs(elem-nb) #new diff #
            resultat = elem
        elif (abs(elem-nb) == diff):
            resultat=min(elem, resultat)

    return resultat

#Déclaration de la liste L et de la variable e
L = [16, 2, 25, 8, 12, 31, 2, 56, 58, 63]
e = 50

#Exécution de la fonction
resultat = plus_proche_sequentielle(L,e)
print(resultat)
