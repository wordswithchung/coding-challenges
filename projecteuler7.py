"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
Answer: 104743
"""

def prime_generator(count):
    """Return a list of prime numbers."""

    return [x for x in range(2, count + 2) if all(x % y != 0 for y in range(2, x))]

prime = prime_generator(105000)