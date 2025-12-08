# Question 6

def add_node(node, point, k, cutaxis=0):
    # Si le noeud n'existe pas, nous sommes donc dans une feuille, et il faut créer le noeud
    if node is None:
        node = [point, None, None]
        return node
    
    # (cutaxis + 1) % k ensures correct cycle 0 -> 1 -> 0 -> 1...
    next_axis = (cutaxis + 1) % k

    if point[cutaxis] <= node[0][cutaxis]:
        node[1] = add_node(node[1], point, k, next_axis)
    else:
        node[2] = add_node(node[2], point, k, next_axis)
        
    return node

if __name__ == "__main__":
    # Nous définissons ici juste la racine de l'arbre
    root = [(0,10), None, None]
    k = 2  # Nous travaillons en 2 dimensions
    
    # Point que nous voulons ajouter dans l'arbre
    point = (-10,0)
    
    add_node(root, point, k)
    print(root)
