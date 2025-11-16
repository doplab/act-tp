#Question 3

class Graph:
    def __init__(self, vertices): # permet de créer un graphe lorsqu'on écrit p.ex Graph(6), il faut notamment indiquer le nombre de sommets
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w): # ajoute une arête entre le sommet u et v avec un poids w
        self.graph.append([u, v, w])

    def find(self, parent, i): # Correspond à la fonction Find-set(x) présentée dans le cours
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y): # Correspond à la fonction Union(x,y) présentée dans le cours
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
            
g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)

def kruskal_algo(Graph):
        result = [] # Permettra de stocker le résultat
        i, e = 0, 0 # Index utilisé dans l'algorithme
        
        Graph.graph = sorted(Graph.graph, key=lambda item: item[2]) # Trie les arêtes par poids croissant, étape 1)
        parent = []
        rank = []
        
        
        for node in range(Graph.V): # Cette boucle parcourt tous les sommets du graphe et crée un ensemble pour chacun d'entre eux
            parent.append(node)
            rank.append(0)
          
        # Tant que le nombre d'arêtes est inférieur à V-1, notre sous-graphe n'atteint pas tous les sommets -> on continue
        while e < Graph.V - 1:
            
            u, v, w = Graph.graph[i] # self.graph contient les arêtes par ordre croissant de poids, on commence avec i = 0
            i = i + 1               # puis à l'itération suivante on voudra avoir la 2ème arête la plus légère, donc on incrémente.
                
            x = Graph.find(parent, u) # Ces 2 lignes des codes permettent de rechercher et de stocker à quel ensemble 
            y = Graph.find(parent, v) # appartiennent u et v.
            
            if x != y: # Si u et v font déjà parti du Minimum Spanning Tree, i.e. u et v appartiennent au même ensemble
                       # Alors on ne veut pas ajouter cette arête au minimum spanning-tree, d'ou le x!=y
                e = e + 1 # Si u et v sont d'ensemble différent, on a atteint un sommet de plus donc on incrémente
                result.append([u, v, w]) # On ajoute la nouvelle arête au résultat
                Graph.apply_union(parent, rank, x, y) # On fusionne l'ensemble auquel appartient v à celui auquel appartient u
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight)) # méthode permettant d'afficher le résultat
        
        return result
    
kruskal_algo(g)