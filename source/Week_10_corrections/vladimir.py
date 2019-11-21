from math import exp

def probability_prison(pi):
    return 1/(1+exp(-pi/5)) - 1/2

def markov_chain(i,pi, T):
    sum = 0
    j = 1
    while j <= int(T):
        r = pi**2
        i = i *(1 + r)
        pi = i /10000
        sig = probability_prison(pi)
        sum += sig
        j+=1
    return i, sum/T
    j += 1

i = 1
T = 5
pi = i / 10000

print(markov_chain(i,pi, T))
