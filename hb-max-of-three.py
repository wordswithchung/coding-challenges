"""
Define a function max_of_three that takes in three numbers as arguments and
returns the largest of them.

>>> max_of_three(1, 5, 2)
5

>>> max_of_three(10, 1, 11)
11
"""

# another potential solution is to .sort() a list and return the [-1] item

def max_of_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3