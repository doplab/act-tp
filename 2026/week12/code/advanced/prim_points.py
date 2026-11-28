def distance_manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def cout_minimal_prim(points):
    # complétez ici
    pass

if __name__ == '__main__':
    points = [[0, 0], [1, 3], [4, 1], [5, 5], [2, 6]]
    print(cout_minimal_prim(points))
    # Résultat attendu : 17
