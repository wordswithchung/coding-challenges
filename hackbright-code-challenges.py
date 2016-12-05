def coins(num_coins):
    """Find change from combinations of `num_coins` of dimes and pennies.

    This should return a set of the unique amounts of change possible.

    You have an endless supply of dimes and pennies. How many different
    amounts of total change can you make using exactly num_coins number coins?

    For example, when num_coins = 3, you can create 4 different kinds of change:

        >>> coins(3) == {3, 12, 21, 30}
        True

        >>> coins(1) == {1, 10}
        True

        >>> coins(2) == {2, 11, 20}
        True

        >>> coins(4) == {4, 13, 22, 31, 40}
        True

        >>> coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
        True
    """

    p = 1 # penny
    d = 10 # dime
    results = set()

    for i in range(num_coins + 1):
        results.add((i * p) + (d * (num_coins - i)))

    return results


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?

        >>> is_anagram_of_palindrome("a")
        True

        >>> is_anagram_of_palindrome("ab")
        False

        >>> is_anagram_of_palindrome("aab")
        True

        >>> is_anagram_of_palindrome("arceace")
        True

        >>> is_anagram_of_palindrome("arceaceb")
        False
    """

    # okay to have one odd character, but everything else needs to be even

    d = {}

    for c in word:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    odd = [i for i in d.values() if i % 2 != 0] # odd characters in dict

    if len(odd) > 1:
        return False
    else:
        return True


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