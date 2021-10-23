
def recherche_binaire_recursive(L, s, r, x):
    if r >= s:
        mid = int((s + r)/2)
        print(f'Le milieu de la liste {L} est {L[mid]} situé à l\'indice {mid}')
        if L[mid] == x:
            return mid
        elif L[mid] > x:
            return recherche_binaire_recursive(L, s, mid-1, x)
        else:
            # on peut aussi utiliser mid mais mid+1 evite une comparaison
            # de plus car cette comparaison est faite en amont
            return recherche_binaire_recursive(L, mid+1, r, x)
    else:
        return -1

L=[1,3,4,5,7,8,9,15]
s = 0
r = len(L)-1 #8 --> première moitié = 4 -->"7" in L --> 7>5 --> deuxième moitié = (0+4)/2 = 2, etc.
x = 8
print(recherche_binaire_recursive(L,s, r, x))
