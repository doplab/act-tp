# Question 5

root = [(0,10), None, None] #Nous définissons ici juste la racine de l'arbre
k = 2 # Ici nous travaillerons en 2 dimensions
point = (-10,0) #Point que nous voulons ajouter dans le graphe

def add_node(node,point,cutaxis = 0):
    
    if node is None: #Si le noeud n'existe pas, nous sommes donc dans une feuille, et il faut créer le noeud
        node = [point,None,None]
        return node
    
    if point[cutaxis] <= node[0][cutaxis]: #1 Se référer aux diapositives du cours
        node[1] = add_node(node[1], point, cutaxis + 1 % k) 
        
    else:
        node[2] = add_node(node[2], point, cutaxis + 1 % k)
        
    return node

add_node(root,point)

print(root)