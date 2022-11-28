def recherche_binaire_iterative(liste,s,r,x):
    while s <= r:
        mid = int(s + (r-s)/2)
        print(f"La moitié correspond à {mid}")
        # if x is present at mid
        if liste[mid] == x:
            print("X dans liste à l'index: ", mid)
            return mid
        # If x is greater, ignore left half
        elif liste[mid] < x:
            s = mid+1
        # If x is smaller, ignore right half
        else:
            r= mid-1
    # If we reach here, then the element was not present
    print("X absent de liste")
    return -1

L = [1,3,4,5,7,8,9,15]
s = 0
r = len(L)
print(f"La liste contient {r} éléments")
x = 6
recherche_binaire_iterative(L,s, r, x)
