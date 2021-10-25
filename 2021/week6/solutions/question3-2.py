
def recherche_binaire_iterative(liste,s,r,x):
    #SOLUTION
    while s <= r:
        mid = int(s + (r-s)/2)
        print(f"La moitié correspond à {mid}")
        if liste[mid] == x:
            print("X dans liste à l'index: ", mid)
            return mid
        elif liste[mid] < x:
            s = mid+1
        else:
            r= mid-1
    print("X absent de liste")
    return -1

L = [1,3,4,5,7,8,9,15]
s = 0
r = len(L)
print(f"La liste contient {r} éléments")
x = 16
recherche_binaire_iterative(L,s, r, x)
