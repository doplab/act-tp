
def recherche_binaire_iterative(liste,s,r,x):
    #SOLUTION
    while s <= r: 
        mid = int(s + (r-s)/2) 
        print(mid)
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
x = 15
recherche_binaire_iterative(L,s, r, x)


