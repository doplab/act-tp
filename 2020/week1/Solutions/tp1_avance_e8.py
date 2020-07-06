# Exercice 20
dict = {'fruit': 'banane', 'legume': 'carotte'}

nouveau_dict = {v: k for k, v in dict.items()}
# On parcourt le dictionnaire d, on recupère chaque élément et renvoie un dictionnaire comprenant la valeur et la clé de chaque élément trouvé dans le dictionnaire.
print(nouveau_dict)
