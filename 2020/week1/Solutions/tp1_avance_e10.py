# Exercice 22
with open('enseignants.txt', 'r') as f:
    l = ['.'.join(line.strip().split()) + '@unil.ch' for line in f.readlines()]
    print('\n'.join(l))
# L'instruction with open() permet de lire un fichier. Le fichier défini comme argument doit se trouver dans le même répertoire que le fichier python. Le second argument de la fonction open() spécifie le mode dans lequel le fichier sera ouvert. Ici, le fichier est ouvert en mode lecture seule (Read only).
# L'instruction f.readlines() retourne toutes les lignes du fichier f sous forme de liste. Chaque ligne est stockée dans la variable line.
# strip() permet de supprimer les espaces superflus qui pourraient exister au début et à la fin de chaque ligne
# split() permet de diviser chaque ligne en mots et join() lie chaque mot avec un point ('.')
# Le résultat est enfin concatené à une chaîne de caractère ('@unil.ch')
