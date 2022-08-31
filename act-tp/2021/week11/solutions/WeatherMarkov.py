import random


def sim_markov_dict(mu_0, P, n_iters):
    
    # liste d'etats
    states = list(mu_0.keys())
    
    # premier etat
    current_state = random.choices(states, list(mu_0.values()))[0]
    
    future_states = []
    for i in range(n_iters):
        next_probs = list(P[current_state].values())
        next_state = random.choices(states, next_probs)[0]
        future_states.append(next_state)
        current_state = next_state
    return future_states
       
mu_0 = {'Sunny': 0.3, 'Snowy': 0.2, 'Rainy': 0.5}
prob_transition = {
    'Sunny': {'Sunny': 0.8, 'Rainy': 0.19,  'Snowy': 0.01},
    'Rainy': {'Sunny': 0.2, 'Rainy': 0.7, 'Snowy': 0.1},
    'Snowy': {'Sunny': 0.1, 'Rainy': 0.2, 'Snowy': 0.7}
}

sim_markov_dict(mu_0, prob_transition, 50)