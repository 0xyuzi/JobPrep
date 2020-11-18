# Preparing for DS

## Sampling
Random weighted sampling with replacement 
    - [Code](./weight_random_sample.py)
    - Has N itmes each with weight in weights list
    - Normalize the weights 
    - Cumulative sum of the weights, cum_weights
    - Generate random sample p from Uni[0,1]
    - if p < cum_weights[i], return the ith item  