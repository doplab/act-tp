liste = [3,6,9,18]

for i in liste:
    if recherche_arbre(root, i) == 0: #Lorsque la fonction retourne "false"
        tree.insert(i,root)
        print(str(i)+" a été ajouté à l'arbre")
 
