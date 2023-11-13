# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

import sympy
from itertools import count
from more_itertools import take

# Get the sum of the first 12 prime numbers
primes = [sympy.prime(x) for x in range(1, 13)]
print(primes)
sum(primes)

# Get the sum of all prime numbers between 80 and 110
primes = [x for x in range(80, 111) if sympy.isprime(x)]
print(primes)
sum(primes)

# Get the sume of the first 11 prime numbers and first 9 composite numbers
primes = [sympy.prime(x) for x in range(1, 12)]
print(primes)
composites = [sympy.composite(x) for x in range(1, 10)]
print(composites)
sum(primes) + sum(composites)

# What is the sum of all the prime numbers between 100 and 130?
primes = [x for x in range(100, 131) if sympy.isprime(x)]
print(primes)
sum(primes)
