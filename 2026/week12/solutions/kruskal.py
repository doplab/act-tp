# Question 4

class Graph:
    def __init__(self, vertices): # permet de créer un graphe lorsqu'on écrit p.ex. Graph(6), il faut notamment indiquer le nombre de sommets
        self.V = vertices # le nombre de sommets
        self.edges = [] # liste de tuples (u, v, w) ou w est le poids de l'arête entre u et v
        self.parent = list(range(vertices)) # une liste [0, .., vertices - 1]
        self.rank = [0]*vertices # une liste [0, ..,0] de longueur vertices  

    def add_edge(self, u, v, w): # ajoute une arête entre le sommet u et v avec un poids w
        self.edges.append((u, v, w))

    def find(self, i): # Correspond à la fonction Find-set(x) du cours
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y): # Correspond à la fonction Union(x,y) du cours
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return False # x et y appartiennent déjà au même ensemble, on ne peut pas fusionner leurs ensembles

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

        return True  # x et y n'appartiennent pas au même ensemble, on peut fusionner leurs ensembles
            
def kruskal(g : Graph):
        result = [] 
        edges = sorted(g.edges, key=lambda item: item[2]) # trie les arêtes par poids croissant
        i = 0 # l'étape de l'itération
        e = 0 # nombre d'arêtes pendant la construction de l'ACM
          
        # Tant que le nombre d'arêtes est inférieur à V-1, notre sous-graphe n'atteint pas tous les sommets -> on continue
        while e < g.V - 1:
            u, v, w = edges[i] # self.graph contient les arêtes par ordre croissant de poids, on commence avec i = 0
            i = i + 1 # à l'itération suivante on voudra avoir la 2ème arête la plus légère, donc on incrémente
                
            if g.union(u, v): # Si u et v font déjà parti du Minimum Spanning Tree, i.e. u et v appartiennent au même ensemble
                       # Alors on ne veut pas ajouter cette arête au minimum spanning-tree
                e = e + 1 # Si u et v sont d'ensemble différent, on a atteint un sommet de plus donc on incrémente
                result.append([u, v, w]) # On ajoute la nouvelle arête au résultat
        
        return result
    
if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 2)
    g.add_edge(3, 4, 3)
    g.add_edge(2, 5, 2)
    g.add_edge(4, 5, 3)
    
    result = kruskal(g)

    for u, v, weight in result:
        print(f"{u} - {v}: {weight}") # afficher le résultat