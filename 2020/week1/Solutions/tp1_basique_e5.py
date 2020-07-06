# Exercice 5
print([x * 3 for x in range(11)])
print(list(map(lambda x: x * 3, range(11))))
# La fonction map prend en argument une fonction (ici définie sous la forme d'une fonction lambda) et une liste (range(11)). Elle retourne la liste composée des éléments de la liste auxquels on a appliqué la fonction lambda
