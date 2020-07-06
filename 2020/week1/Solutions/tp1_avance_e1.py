# Exercice 13
l = ['a', 'b', 'c']
print('_'.join(l))
print(reduce(lambda x, y: x + '_' + y, l))
# La fonction join(l) permet de lier tous les éléments de la liste l avec pour séparateur '_'
# La fonction lambda, couplée à reduce fait la même opération en concaténant l'élément i de la liste l avec l'élément i+1 et un séparateur ('_').
