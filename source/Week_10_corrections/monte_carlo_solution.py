def evaluate_pi(iterations):
    inside = 0
    for i in range(iterations):
        x, y = (uniform(0, 1), uniform(0, 1))
        if x**2 + y** 2 <= 1:
            inside += 1
    return (inside/iterations)*4


def integrale(function, _min = 0, _max = 1, iterations = 100000):
    total = 0
    for i in range(iterations):
        rand_x = uniform(_min, _max)
        total += function(rand_x)
    return total/iterations
