# Exercice 15
l1 = ['Claire Bilat', 'Dario Besson', 'David Salathé', 'Kai Eckert', 'Matthieu Baud']
l2 = ['UNIL', 'UNIL', 'EPFL', 'UNIL', 'EPFL']

print('\n'.join([etudiant for (etudiant, ecole) in list(zip(l1, l2)) if ecole == 'UNIL']))
# La fonction zip associe un élément d'une liste à un autre et retourne un tuple composé des deux éléments
# Créer une liste de couples à partir des éléments des listes names et schools
# join permet de lier les éléments de la liste l avec pour séparateur un retour chariot défini par '\n'
