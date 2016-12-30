def highest_product_of_3(a):
    """Given a list of integers (a), return the highest product of 3
    integers in the list.

    """

    if len(a) < 3:
        raise Exception("Less than 3 items!")

    highest = max(a[0], a[1])
    highest_product_of_2 = a[0] * a[1]

    lowest = min(a[0], a[1])
    lowest_product_of_2 = a[0] * a[1]

    highest_product_of_3 = a[0] * a[1] * a[2]

    for current in a[2:]:
        highest_product_of_3 = max(highest_product_of_3,
                                   current * highest_product_of_2,
                                   current * lowest_product_of_2)

        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest, current * lowest)

        lowest_product_of_2 = min(lowest_product_of_2,
                                  current * highest, current * lowest)

        highest = max(highest, current)

        lowest = min(lowest, current)

    return highest_product_of_3
