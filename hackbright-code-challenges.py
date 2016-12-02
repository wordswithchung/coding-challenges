def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0.

        >>> add_to_zero([0, 1, 2])
        True

        >>> add_to_zero([])
        False

        >>> add_to_zero([1])
        False

        >>> add_to_zero([1, 2, 3])
        False

        >>> add_to_zero([1, 2, 3, -2])
        True
    """

    for num in nums:
        if num == 0:
            return True
        elif -num in nums:
            return True

    return False


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
    # v1
    # return list1 + list2

    # v2
    for i in list2:
        list1.append(i)

    return list1


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