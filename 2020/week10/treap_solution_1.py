from random import randrange

# Un noeud de la treap
class TreapNode:
	def __init__(self, data, priority=100, left=None, right=None):
		self.data = data
		self.priority = randrange(priority)
		self.left = left
		self.right = right

# Fonction pour faire une rotation à gauche
def rotateLeft(root):

	R = root.right
	X = root.right.left

	# rotate
	R.left = root
	root.right = X

	# set root
	return R


# Fonction pour faire une rotation à droite
def rotateRight(root):

	L = root.left
	Y = root.left.right

	# rotation
	L.right = root
	root.left = Y

	# retourne la nouvelle racine
	return L
