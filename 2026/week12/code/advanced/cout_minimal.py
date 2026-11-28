class Graph: # même structure Union-Find que dans kruskal.py
    def __init__(self, vertices):
        self.V = vertices
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y): # retourne True si x et y étaient dans deux ensembles différents
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return False
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
        return True

def distance_manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def cout_minimal(points):
    # complétez ici
    pass

if __name__ == '__main__':
    points = [[0, 0], [1, 3], [4, 1], [5, 5], [2, 6]]
    print(cout_minimal(points))
    # Résultat attendu : 17
