"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

answer = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i * j
        b = str(a)[::-1]
        if a == int(b):
            answer.append((a, i, j))

print max(answer)