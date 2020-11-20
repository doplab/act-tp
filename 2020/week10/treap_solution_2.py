# Fonction récursive pour insérer une clé avec une priorité dans une Treap
def insertNode(root, data):

	if root is None:
		return TreapNode(data)

    # si data est inférieure à celle la racine root, insérer dans le sous-abre gauche
    # sinon insérer dans le sous-arbre droit
	if data < root.data:
		root.left = insertNode(root.left, data)

		# faire une rotation à droite si la propriété de la heap est violée 
		if root.left and root.left.priority > root.priority:
			root = rotateRight(root)
	else:
		root.right = insertNode(root.right, data)

		# faire une rotation à gauche si la propriété de la heap est violée 
		if root.right and root.right.priority > root.priority:
			root = rotateLeft(root)

	return root


# Affiche les noeuds de la treap
def printTreap(root, space):
	height = 10

	if root is None:
		return

	space += height
	printTreap(root.right, space)

	for i in range(height, space):
		print(' ', end='')

	print((root.data, root.priority))
	printTreap(root.left, space)


if __name__ == '__main__':
	# Clés de la treap
	keys = [5, 2, 1, 4, 9, 8, 10]

	# Construction de la treap
	root = None
	for key in keys:
		root = insertNode(root, key)

	printTreap(root, 0)
