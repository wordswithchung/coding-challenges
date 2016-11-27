def concat_lists1(list1, list2):
    """Combine lists.

        >>> concat_lists1([1, 2], [3, 4])
        [1, 2, 3, 4]
        >>> concat_lists1([], [1, 2])
        [1, 2]
        >>> concat_lists1([1, 2], [])
        [1, 2]
        >>> concat_lists1([], [])
        []
    """

    concat = []

    for i in (list1 + list2):
        if i:
            concat.append(i)

    return concat


def concat_lists2(list1, list2):
    """Combine lists.

        >>> concat_lists2([1, 2], [3, 4])
        [1, 2, 3, 4]
        >>> concat_lists2([], [1, 2])
        [1, 2]
        >>> concat_lists2([1, 2], [])
        [1, 2]
        >>> concat_lists2([], [])
        []
    """

    # same function via list comprehension

    return [i for i in (list1 + list2) if i]


def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

        >>> lst = ["hey", "there", "you"]
        >>> recursive_index("hey", lst)
        0
        >>> recursive_index("you")
        2
        >>> recursive_index("porcupine", lst) is None
        True

    """

    pass



def rev_list_in_place(lst):
    """Reverse list in place.

    You cannot do this with reversed(), .reverse(), or list slice
    assignment!

        >>> lst = [1, 2, 3]
        >>> rev_list_in_place(lst)
        >>> lst
        [3, 2, 1]
    """

    # fundamental thing is to take first item, append it, then remove it
    # or take the last item, insert it to the front, then pop the last
    # base case is when the lst is done

    lst.insert(0, lst[-1])
    lst.pop

    pass

"""
Write a function the returns True or False, depending on whether the integer
passed into it is a prime number.

Only numbers >1 can be prime numbers:

>>> is_prime(0)
False

>>> is_prime(1)
False

Any number >1 that has no divisors other than 1 and itself is a prime number:

>>> is_prime(2)
True

>>> is_prime(3)
True

>>> is_prime(4)
False

>>> is_prime(11)
True

>>> is_prime(999)
False
"""

def primes_list_comprehension():
    """Return count number of prime numbers, starting at 2."""
    # http://stackoverflow.com/a/31045603

    return [x for x in range(2, count + 2) if
            all(x % y != 0 for y in range(2, x))]


#####################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

