import random

def sim_markov_dict(mu_0, P, n_iters):    
    # liste d'etats
    states = list(mu_0.keys())
    # premier etat
    current_state = ... # Partie à compléter
    future_states = []
    ... # Partie à compléter
        
    return ... # Partie à compléter
       
mu_0 = {'Sunny': 0.3, 'Snowy': 0.2, 'Rainy': 0.5}
prob_transition = {
    'Sunny': {'Sunny': 0.8, 'Rainy': 0.19,  'Snowy': 0.01},
    'Rainy': {'Sunny': 0.2, 'Rainy': 0.7, 'Snowy': 0.1},
    'Snowy': {'Sunny': 0.1, 'Rainy': 0.2, 'Snowy': 0.7}
}

sim_markov_dict(mu_0, prob_transition, 50)