import numpy as np

import random
from random import random 

def weighted_choice(objects, weights):
    """ returns randomly an element from the sequence of 'objects', 
        the likelihood of the objects is weighted according 
        to the sequence of 'weights', i.e. percentages."""

    weights = np.array(weights, dtype=np.float64)
    sum_of_weights = weights.sum()
    # standardization:
    np.multiply(weights, 1 / sum_of_weights, weights)
    weights = weights.cumsum()
    x = random()
    for i in range(len(weights)):
        if x < weights[i]:
            return objects[i]


# main
from collections import Counter 
a = [i for i in range(3)]
weights= [5, 3, 2]

n = 10000
res = []
for _ in range(n):
    res.append(weighted_choice(a,weights))

counter = Counter(res)
print(counter) 

