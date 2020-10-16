
    def recherche_binaire_recursive(liste,s,r,x): #s as first index and r as last index of liste
        #SOLUTION
        mid = int((s+r)/2) #int arrondi vers le bas
        print(mid)
        if liste[mid] < x:
            return recherche_binaire_recursive(liste, mid, r, x) 
        elif liste[mid] > x:
            return recherche_binaire_recursive(liste, s, mid, x)
        elif liste[mid] == x:
            print("X in liste at index: ", mid)
            return mid 
        else:
            print ("X not in liste")
            
    L=[1,3,4,5,7,8,9,15]
    s = 0
    r = len(L) #8 --> first mid = 4 -->"7" in L --> 7>5 --> new mid = (0+4)/2 = 2, etc.
    x = 5
    recherche_binaire_recursive(L,s, r, x)
    
    
   
    