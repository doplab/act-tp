def recherche_binaire(liste,e):
    first = 0 #correspond à l'index du premier élément de la liste
    last = len(liste)-1 #correspond à l'index du dernier élément de la liste
    #SOLUTION
    while first <= last:
        mid = int((first+last)/2) #l'élément du milieu. La fonction int() permet d'obtenir un entier dans le cas ou "first + last" est un nombre impair
        print(mid)
        if liste[mid] == e:
            return mid #Si la condition est juste, la fonction retourne l'index de la valeur recherchée dans la liste
        else:
            if liste[mid] > e:
                last -= 1
            else:
                first +=1
    return False # Si la condition de la ligne 8 n'est jamais remplie, la fonction retourne "False" 

L = [1231321,3213125,3284016,4729273,5492710]
e = 3284016
recherche_binaire(L,e)

%%time
print(recherche_binaire(L,e))