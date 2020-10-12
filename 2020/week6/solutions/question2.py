#Definition de la fonction ayant pour argument une liste et un nombre 
def plus_proche_sequentielle(liste,n):
    diff = None #Initialisation de la variable pour la différence
    resultat = None #Initialisation de la variable pour le résultat
    
    #Solution
    for i in liste:
        if not diff or abs(i-n) < diff: #old diff
            diff = abs(i-n) #new diff # 
            resultat = i
            
    return resultat, diff

#Déclaration de la liste L et de la variable e
L = [16, 2, 25, 8, 12, 31, 2, 56, 58, 63]  
e = 50

#Exécution de la fonction
plus_proche_sequentielle(L,e)

%%time 
print(plus_proche_sequentielle(L,e))