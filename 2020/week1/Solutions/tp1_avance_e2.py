# Exercice 14
def lister_int(n):
    return ','.join([str(x) for x in range(1, n + 1)])

print((lister_int(10)))
# La fonction join(l) permet de lier tous les éléments de la liste générée à travers l'instruction 'range(1, n + 1)' en utilisant comme séparateur ','
