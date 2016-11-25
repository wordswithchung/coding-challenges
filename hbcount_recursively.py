def count_recursively(lst):
    """Count the number of items in a list, using recursion.

        >>> count_recursively([])
        0
        >>> count_recursively([1, 2, 3])
        3
    """

    # if something, count = 1
    if lst:
        return 1 + count_recursively(lst[1:])
    else:
        return 0