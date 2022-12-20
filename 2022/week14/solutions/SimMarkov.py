import random


def sim_markov(mu_0, P, n_iters=500):
    # mu_0 (n,1) # probabilités initiales - n états
    # P (n, n) # matrice de transition

    states = range(len(mu_0))  # e.g si la longueur de mu_0 est 2, on aura 2 états 0, 1
    X0 = random.choices(states, mu_0)[0]
    print(random.choices(states, mu_0))

    future_states = []
    future_states.append(X0)
    for i in range(n_iters):
        next_state = random.choices(states, P[future_states[i]])[0]
        future_states.append(next_state)

    return future_states


P = [[0.1, 0.9],
     [0.7, 0.3]]

mu_0 = [0.3, 0.7]

print(sim_markov(mu_0, P))
