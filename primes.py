import itertools
import sympy as sym

def take(n, iterator):
	for i in iterator:
		yield i
		n -= 1
		if n == 0:
			break

def get_primes(start=2):
	return (i for i in itertools.count(start) if sym.simplify(i).is_prime)

def get_composites(start=4):
	return (i for i in itertools.count(start) if sym.simplify(i).is_composite)


primes = list(take(12, get_primes()))
print(primes)
print(sum(primes))
print(sum(primes) * 0.25)

primes = list(itertools.takewhile(lambda x: x < 110, get_primes(80)))
print(primes)
print(sum(primes))

primes = list(take(11, get_primes()))
print(primes)
composites = list(take(9, get_composites()))
print(composites)
print(sum(primes) * sum(composites))
