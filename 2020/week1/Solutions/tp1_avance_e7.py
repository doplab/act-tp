# Exercice 19
noms = [['John', 'Ronald', 'Reuel', 'Tolkien'], ['Noe', 'Zufferey'], ['Claire', 'Oceane', 'Roxane', 'Billat'], ['Melike', 'Gwendoline', 'Alice', 'Gecer']]
x = ', '.join(sorted([l[0] + (' ' if len(l) > 2 else '') + ' '.join(map(lambda s: s[0].capitalize() + '.', l[1:-1])) + ' ' + l[-1] for l in noms], key=lambda n: n[-1]))
# Sorted permet de trier une liste, le paramètre key prend en entrée une fonction qui sera utilisée comme clé permettant de faire le tri. Dans notre cas, la fonction lambda utilisée retourne le dernier élément d'une liste
print(x)
