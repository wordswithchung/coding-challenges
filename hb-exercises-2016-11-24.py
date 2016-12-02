def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    vowels = {'a', 'e', 'i', 'o', 'u'}

    pig_latin_phrase = []

    phrase = phrase.split(' ')

    for word in phrase:
        if word[0] in vowels:
            pig_latin_phrase.append(word + 'yay')
        else:
            pig_latin_phrase.append(word[1:] + word[0] + 'ay')

    return ' '.join(pig_latin_phrase)

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses.

        >>> binary_search(50)
        1

        >>> binary_search(25)
        2

        >>> binary_search(75)
        2

        >>> binary_search(31) <= 7
        True

        >>> max([binary_search(i) for i in range(1, 101)])
        7
    """

    # assert 0 < val < 101, "Val must be between 1-100"

    # num_guesses = 0

    # return num_guesses
    pass

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

    return list1 + list2


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

