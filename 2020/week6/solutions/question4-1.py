
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
    
    
   
    
