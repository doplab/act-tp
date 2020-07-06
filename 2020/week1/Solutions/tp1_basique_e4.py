# Exercice 4
print([x for x in range(11) if x % 2 != 0])
# for x in range(10) permet de générer une suite de nombres allant de 0 à 10
print(list(filter(lambda x: x % 2 != 0, range(11))))
