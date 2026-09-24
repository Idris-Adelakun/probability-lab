import math
from numpy import random as npr

def disrecte_rv(values, probabilities):
    Ex = 0
    Ex2 = 0
    Var = 0

    if len(values) != len(probabilities):
        raise ValueError("List lengths do not match")


    if  not math.isclose(sum(probabilities), 1.0):
        raise ValueError("Probabilities must sum to 1")


    for value, probability in zip(values, probabilities):
        Ex += value * probability
        Ex2 += value**2 * probability

    Var = Ex2 - Ex**2

    return f"Ex: {Ex}\n Ex^2:{Ex2}\n Var(x):{Var}" 


print(disrecte_rv([1, 2], [0.5, 0.5]))