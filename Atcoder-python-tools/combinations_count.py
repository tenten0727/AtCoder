from math import factorial

def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))