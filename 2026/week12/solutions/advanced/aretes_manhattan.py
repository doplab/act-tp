def distance_manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

def construire_aretes(points):
    aretes = []
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n): # j > i : chaque paire n'est considérée qu'une fois
            w = distance_manhattan(points[i], points[j])
            aretes.append((i, j, w))
    return aretes

if __name__ == '__main__':
    print(distance_manhattan([1, 3], [4, 1]))
    points = [[0, 0], [1, 3], [4, 1]]
    print(construire_aretes(points))
