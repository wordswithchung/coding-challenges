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


#####################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

