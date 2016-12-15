def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place.

        >>> print_digits(1)
        1
        >>> print_digits(314)
        4
        1
        3
        >>> print_digits(12)
        2
        1
    """

    while num % 10 != num:
        m = num % 10
        print m
        num = (num - m) / 10

    print num


# def max_num(num_list):
#     """Returns largest integer from given list

#         >>> max_num([5, 3, 6, 2, 1])
#         6
#     """

#     i = num_list[0]

#     for num in num_list[1:]:
#         if num > i:
#             i = num

#     return i

# def has_balanced_parens(mystr):
#     """Given a string, returns True or False depending on whether that
#        string has balanced parentheses.

#         >>> has_balanced_parens("()")
#         True

#         >>> has_balanced_parens("(Oh Noes!)(")
#         False

#         >>> has_balanced_parens("((There's a bonus open paren here.)")
#         False

#         >>> has_balanced_parens(")")
#         False

#         >>> has_balanced_parens("(")
#         False

#         >>> has_balanced_parens("Hey...there are no parens here!")
#         True
#     """

#     count = 0

#     for i in mystr:
#         if i == '(':
#             count += 1
#         elif i == ')':
#             count -= 1

#     if count == 0:
#         return True
#     elif count < 0 or count > 0:
#         return False

# def find_largest_smaller_than(nums, xnumber):
#     """In a sorted list of nums, find largest number that is smaller than
#     xnumber, returns None if not found

#         >>> find_largest_smaller_than([-5, 8, 12, 32], 10)
#         1

#         >>> find_largest_smaller_than([-5, 8, 12, 32], 33)
#         3

#         >>> find_largest_smaller_than([-5, 8, 12, 32], -7)
#         None

#         >>> find_largest_smaller_than([-5, 8, 12, 32], 7)
#         0
#     """

#     for num in nums[::-1]:
#         if num > xnumber:
#             return nums.index(num) - 1

#     return -1

# def has_unique_chars(word):
#     """Given a word, return True if that word contains a unique set of
#     characters. Return False otherwise.

#         >>> has_unique_chars("Monday")
#         True

#         >>> has_unique_chars("Moonday")
#         False

#         >>> has_unique_chars("")
#         True
#     """

#     if not word:
#         return True

#     s = set()

#     for i in word:
#         if i not in s:
#             s.add(i)
#         else:
#             return False

#     return True


# def fizzbuzz():
#     """Count from 1 to 20 in fizzbuzz fashion. To do so, loop from 1 to 20
#     (inclusive). Each time through, if the number is evenly divisible by 3,
#     say 'fizz'. If the number is evenly divisible by 5, say 'buzz'. If the
#     number is evenly divisible by both 3 and 5, say 'fizzbuzz'. Otherwise,
#     say the number.

#         >>> fizzbuzz()
#         1
#         2
#         fizz
#         4
#         buzz
#         fizz
#         7
#         8
#         fizz
#         buzz
#         11
#         fizz
#         13
#         14
#         fizzbuzz
#         16
#         17
#         fizz
#         19
#         buzz
#     """

#     for i in range(1, 21):
#         if i % 3 == 0 and i % 5 == 0:
#             print 'fizzbuzz'
#         elif i % 3 == 0:
#             print 'fizz'
#         elif i % 5 == 0:
#             print 'buzz'
#         else:
#             print i


# def rev_list_in_place(lst):
#     """Reverse list in place.

#     You cannot do this with reversed(), .reverse(), or list slice
#     assignment!

#         >>> lst = [1, 2, 3]
#         >>> rev_list_in_place(lst)
#         >>> lst
#         [3, 2, 1]
#     """

#     for i in range((len(lst) / 2)):
#         lst[i], lst[-i - 1] = lst[-i - 1], lst[i]


# def coins(num_coins):
#     """Find change from combinations of `num_coins` of dimes and pennies.

#     This should return a set of the unique amounts of change possible.

#     You have an endless supply of dimes and pennies. How many different
#     amounts of total change can you make using exactly num_coins number coins?

#     For example, when num_coins = 3, you can create 4 different kinds of change:

#         >>> coins(3) == {3, 12, 21, 30}
#         True

#         >>> coins(1) == {1, 10}
#         True

#         >>> coins(2) == {2, 11, 20}
#         True

#         >>> coins(4) == {4, 13, 22, 31, 40}
#         True

#         >>> coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
#         True
#     """

#     p = 1 # penny
#     d = 10 # dime
#     results = set()

#     for i in range(num_coins + 1):
#         results.add((i * p) + (d * (num_coins - i)))

#     return results

# def is_palindrome(word):
#     """Return True/False if this word is a palindrome.

#         >>> is_palindrome("a")
#         True

#         >>> is_palindrome("noon")
#         True

#         >>> is_palindrome("racecar")
#         True

#         >>> is_palindrome("porcupine")
#         False

#         >>> is_palindrome("Racecar")
#         False
#     """

#     for i in range(len(word) / 2):
#         if word[i] != word[-i - 1]:
#             return False

#     return True

# def is_anagram_of_palindrome(word):
#     """Is the word an anagram of a palindrome?

#         >>> is_anagram_of_palindrome("a")
#         True

#         >>> is_anagram_of_palindrome("ab")
#         False

#         >>> is_anagram_of_palindrome("aab")
#         True

#         >>> is_anagram_of_palindrome("arceace")
#         True

#         >>> is_anagram_of_palindrome("arceaceb")
#         False
#     """

#     # okay to have one odd character, but everything else needs to be even

#     d = {}

#     for c in word:
#         if c in d:
#             d[c] += 1
#         else:
#             d[c] = 1

#     odd = [i for i in d.values() if i % 2 != 0] # odd characters in dict

#     if len(odd) > 1:
#         return False
#     else:
#         return True


# def add_to_zero(nums):
#     """Given list of ints, return True if any two nums sum to 0.

#         >>> add_to_zero([0, 1, 2])
#         True

#         >>> add_to_zero([])
#         False

#         >>> add_to_zero([1])
#         False

#         >>> add_to_zero([1, 2, 3])
#         False

#         >>> add_to_zero([1, 2, 3, -2])
#         True
#     """

#     for num in nums:
#         if num == 0:
#             return True
#         elif -num in nums:
#             return True

#     return False


# def concat_lists2(list1, list2):
#     """Combine lists.

#         >>> concat_lists2([1, 2], [3, 4])
#         [1, 2, 3, 4]
#         >>> concat_lists2([], [1, 2])
#         [1, 2]
#         >>> concat_lists2([1, 2], [])
#         [1, 2]
#         >>> concat_lists2([], [])
#         []
#     """
#     # v1
#     # return list1 + list2

#     # v2
#     for i in list2:
#         list1.append(i)

#     return list1


# def pig_latin(phrase):
#     """Turn a phrase into pig latin.

#     There will be no uppercase letters or punctuation in the phrase.

#         >>> pig_latin('hello awesome programmer')
#         'ellohay awesomeyay rogrammerpay'
#     """

#     vowels = {'a', 'e', 'i', 'o', 'u'}

#     pig_latin_phrase = []

#     phrase = phrase.split(' ')

#     for word in phrase:
#         if word[0] in vowels:
#             pig_latin_phrase.append(word + 'yay')
#         else:
#             pig_latin_phrase.append(word[1:] + word[0] + 'ay')

#     return ' '.join(pig_latin_phrase)