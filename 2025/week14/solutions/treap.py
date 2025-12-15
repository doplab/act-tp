## Copiez le code de treap.py de la ligne 1 à 75 dans le dossier Moodle code/treap.py 

root = None
treap = Treap()

liste = [5, 2, 1, 4, 9, 8, 10]
nodes = []

# Création de la liste de noeuds + priorités
for i in liste:
    pair = (i, random.randrange(100))
    nodes.append(pair)

print(f"Noeuds avant insertion: {nodes}")

# Construction du treap
for j in nodes:
    treap.insert(j[0], j[1], root)

print(f"Treap: {treap}")
