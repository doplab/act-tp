def recherche_binaire_iterative(liste,s,r,x):
    while s <= r:
        mid = int(s + (r-s)/2)
        print(f"La moitié correspond à {mid}")
        # Si l'élément du milieu correspond à x, on retourne mid
        if liste[mid] == x:
            print("X dans liste à l'index: ", mid)
            return mid
        # Si x est plus grand, on ignore la moitié de gauche
        elif liste[mid] < x:
            s = mid+1
        # Si x est plus petit, on ignore la moitié de droite
        else:
            r= mid-1
    # Si on sort de la boucle, c'est que l'élément est absent de la liste
    print("X absent de liste")
    return -1

L = [1,3,4,5,7,8,9,15]
s = 0
r = len(L)
print(f"La liste contient {r} éléments")
x = 6
recherche_binaire_iterative(L,s, r, x)
