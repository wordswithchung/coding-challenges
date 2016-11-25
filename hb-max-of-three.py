def max_of_three(num1, num2, num3):
    """
    Define a function max_of_three that takes in three numbers as arguments and
    returns the largest of them.

    >>> max_of_three(1, 5, 2)
    5

    >>> max_of_three(10, 1, 11)
    11
    """
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


def max_of_three_v2(num1, num2, num3):
    """Function takes in three numbers as arguments and returns the lartest.

        >>> max_of_three_v2(8, 5, 55)
        55
    """

    lst = [num1, num2, num3]
    lst.sort()

    return lst[-1]


#####################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

