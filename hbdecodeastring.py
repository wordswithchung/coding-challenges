def decode(s):
    """Decode a string.

    A valid code is a sequence of numbers and letters, always starting with a
    number and ending with letter(s).

    Each number tells you how many characters to skip before finding a good
    letter. After each good letter should come the next next number.

    For example, the string 'hey' could be encoded by '0h1ae2bcy'. This means
    "skip 0, find the 'h', skip 1, find the 'e', skip 2, find the 'y'".

    A single letter should work:

        >>> decode("0h")
        'h'

        >>> decode("2abh")
        'h'

        >>> decode("0h1ae2bcy")
        'hey'
    """

    good = []
    skip = None
    nums = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

    for i in s:
        if i in nums:
            skip = int(i)
        else:
            if skip > 0:
                skip -= 1
            else:
                good.append(i)

    return ''.join(good)



