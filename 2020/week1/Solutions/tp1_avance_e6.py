# Exercice 18
def convertir_noms(l):
    # l[1:-1] renvoie la sous-liste partant du deuxième élément jusqu'au dernier (non inclus)
    return l[0] + (' ' if len(l) > 2 else '') + ' '.join(map(lambda s: s[0].capitalize() + '.', l[1:-1])) + ' ' + l[-1]

print(convertir_noms(['John', 'Ronald', 'Reuel', 'Tolkien']))
