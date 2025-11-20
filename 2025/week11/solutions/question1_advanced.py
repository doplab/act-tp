def plus_proche_binaire(liste, n):
    # SOLUTION
  
    min = 0
    max = len(liste) 
    
    if(n >= liste[max - 1]):
        return liste[max -1]
    if(n <= liste[min]):
        return liste[min]
    found = False # boolean variable
    while min <= max and not found:  # 0<10 and true puis 6<10 and true, etc.
        mid = (max + min) // 2  # mid = 5 --> 16 in list
        print(mid)
        if n > liste[mid]:  # 41>16
            min = mid + 1  # min = 5+1=6
        elif n < liste[mid]:
            max = mid - 1
        else:
            found = True
    if found:
        return liste[mid]
    else: #min = max + 1 on choisit le plus proche entre min et max 
        if abs(liste[min]-n) < abs(liste[max]-n) :
            return liste[min]
        else:
           return liste[max]
        


L = [1, 2, 5, 8, 12, 16, 24, 56, 58, 63]
e = 60
print(plus_proche_binaire(L, e))
