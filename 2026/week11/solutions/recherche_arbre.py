def recherche_arbre(node, e):
    #Solution
    if node == None:
        return False

    if node.value == e:
        return True
    if node.value > e:
        return recherche_arbre(node.left, e)
    else:
        return recherche_arbre(node.right, e)
