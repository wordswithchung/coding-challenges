"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
https://projecteuler.net/problem=3
"""

def primes_list_comprehension(count):
    """Return count number of prime numbers, starting at 2."""
    # http://stackoverflow.com/a/31045603

    return [x for x in range(2, count + 2) if all(x % y != 0
                                                  for y in range(2, x))]

a = primes_list_comprehension(10000)

factor = []

for i in a[::-1]:
    if 600851475143 % i == 0:
        factor.append(i)

return max(factor)

# answer 6857