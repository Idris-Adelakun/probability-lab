import numpy as np
from math import factorial


def calculate_prob_k_heads(num_heads, num_tosses):
    '''
    Calculate the probability of k heads in n fair tosses
    '''

    n = num_tosses
    k = num_heads

    outcomes = 2**n
    combinations = factorial(n)/(factorial(k)*(factorial(n-k)))

    result  = combinations/outcomes

    return result


