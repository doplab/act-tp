# Exercice 6
print([x * 3 for x in range(11) if x % 2 == 0])
# L'instruction for x in range(11) génère une suite de nombres de 0 à 10 tandis que la condition  vérifie si l'entier est pair ou impair. (x * 3) est exécuté uniquement si la condition est évaluée à True.
print(list(map(lambda x: x * 3, filter(lambda x: x % 2 == 0, range(11)))))
# Filter créé une liste d'éléments en fonction du résultat de la fonction lamda passée en paramètre. Filter récupère uniquement le nombre qui, passé à la fonction lambda, renvoie True.
