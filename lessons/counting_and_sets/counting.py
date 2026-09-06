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


def two_dice_experiment(target_sum):
    '''
    Construct sample space of elementary outcomes and probabilities of specific totals for the experiment of two fair six-sided dice being rolled simultaneously
    '''

    D1 = [1,2,3,4,5,6]
    D2 = [1,2,3,4,5,6]

    sample_space = []
    totals = []
    event = []
   

    for die_1 in D1:
        for die_2 in D2:
            pair = (die_1, die_2)
            sample_space.append(pair)

            total = die_1 + die_2
            totals.append(total)

            if total == target_sum:
                event.append(total)

    probability = len(event)/36

    return probability














