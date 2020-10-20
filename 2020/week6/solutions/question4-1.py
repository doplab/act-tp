
def recherche_binaire_recursive(L, s, r, x): 
    if r >= s: 
        mid = int((s + r)/2)
        if L[mid] == x: 
            return mid 
        elif L[mid] > x: 
            return recherche_binaire_recursive(L, s, mid - 1, x) 
        else: 
            return recherche_binaire_recursive(L, mid + 1, r, x) 
    else:  
        return -1
    
L = [1,3,4,5,7,8,9,15]
s = 0
r = len(L)-1
x = 7
print(recherche_binaire_iterative(L,s, r, x))
   
    
