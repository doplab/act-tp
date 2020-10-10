def tri_bulle(l):
                        for i in range(1, len(l)):
                            # Les i derniers éléments sont dans leur bonne position 
                            for j in range(0, n-i-1): 
                      
                                # parcourir la liste de 0 à n-i-1 
                                # Echanger si l'élément trouvé est supérieur 
                                # au prochain élément
                                if l[j] > l[j+1] : 
                                    l[j], l[j+1] = l[j+1], l[j] 
                    
                    if __name__ == "__main__":
                        l = [1, 2, 4, 3, 1]
                        tri_bulle(l)
                        print(liste_triee)