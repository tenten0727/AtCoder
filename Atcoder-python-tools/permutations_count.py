from math import factorial

def permutations_count(n, r):
    return factorial(n) // factorial(n - r)