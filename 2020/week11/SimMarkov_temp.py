def sim_markov(mu_0, P, n_iters=500):
    # mu_0 (n,1) # probabilités initiales - n états
    # P (n, n) # matrice de transition
    
    states = range(len(mu_0)) # e.g si la longueur de mu_0 est 2, on aura 2 états 0, 1
    ...
    
    
P = [[0.1, 0.9], 
     [0.7, 0.3]]
mu_0 = [0.3, 0.7]
print(sim_markov(mu_0, P))