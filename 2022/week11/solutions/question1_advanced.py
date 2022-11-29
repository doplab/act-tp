def recherche_binaire(liste,e):
    first = 0 #correspond à l'index du premier élément de la liste
    last = len(liste) #correspond à l'index du dernier élément de la liste
    #SOLUTION
    while first <= last:
        mid = int((first+last)/2) #l'élément du milieu. La fonction int() permet d'obtenir un entier dans le cas ou "first + last" est un nombre impair
        # print(mid)
        if liste[mid] == e:
            return mid #Si la condition est juste, la fonction retourne l'index de la valeur recherchée dans la liste
        else:
            if liste[mid] > e:
                last = mid-1
            else:
                first = mid+1
    return -1 # Si la condition de la ligne 8 n'est jamais remplie, la fonction retourne -1 

L = [123, 321, 328, 472, 549]
e = 500
print(recherche_binaire(L,e))

