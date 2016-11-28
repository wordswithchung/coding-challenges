"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

From https://www.mathsisfun.com/pythagorean_triples.html
https://www.mathsisfun.com/numbers/pythagorean-triples.html
The simplest way to create further Pythagorean Triples is to scale up a set
of triples. Example: scale 3,4,5 by 2 gives 6,8,10
"""

def make_pythagorean_triples(n):
    """m must be less than n; both are integers; (hint: n = 20)"""

    for m in range(1, n - 1):
        a = (n ** 2) - (m ** 2)
        b = 2 * n * m
        c = (n ** 2) + (m ** 2)
        if a + b + c == 1000:
            return ("A is {}, B is {}, and C is {}. "
                    "Their product is {}".format(a, b, c, (a * b * c)))