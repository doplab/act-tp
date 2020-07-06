# Exercice 21
d1 = {1: 'pomme', 2: 'fraise'}
d2 = {1: 'fruit', 3: 'legume'}
print([{v:d2[k] for k, v in d1.items() if k in d2}])
# on récupère tous les éléments de d1 (en utilisant d1.items()), l'instruction 'if k in d2' vérifie si la clé de l'élément parcouru se trouve dans le dictionnaire d2. Si la condition est vérifiée, un dictionnaire est créé avec pour clé v (issue de d1) et pour valeur l'élément correspondant à la position de la clé de l'élément utilisé.
