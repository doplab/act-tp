    #Définition de la fonction
    def recherche_sequentielle(liste, x):
        for i in range(len(liste)): #i représente l'index 
            if liste[i] == x:
                print("X est présent dans la liste à l'index :", i)
                return i
                
            else: #Utilisez "else" s'il n'y a pas de "break"
                print("X n'est pas présent dans la liste")
                return -1
    
    #Déclaration de la liste et de la variable x 
    L = [3,55,6,8,3,5,56,33,6,5,3,2,99,53,532,75,21,963,100,445,56,45,12,56,24]
    x = 100
    
    #Exécution de l'algorithme
    recherche_sequentielle(L, x)
  
  