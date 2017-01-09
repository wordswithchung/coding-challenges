"""
#The "Find The Duplicates" Problem

#Given two arrays of US social security numbers: Arr1 and Arr2 of lengths n
#and m respectively, how can you most efficiently compute an array of all
#persons included on both arrays?

#Solve and analyze the complexity for 2 cases:
#1. m ≈ n - lengths are approximately the same
#2. m ≫ n - one is much longer than the other

# scenario #1 where lists are about the same length
# test case [1, 2, 3, 4, 5, 6], [5, 6, 7, 8, 9, 10] >> [5, 6]
"""

def find_dup_1(n, m):
    """n and m are appromimately the same length, so we will loop through
    both lists at the same time, comparing each item.
    """

    duplicates = []

    count_n = 0
    count_m = 0

    while count_n < len(n) and count_m < len(m):
        if n[count_n] == m[count_m]:
            duplicates.append(n[count_n])
        elif n[count_n] < m[count_m]:
            count_n += 1
        else:
            count_m += 1

    return duplicates


def find_dup_2(n, m):
    """Since m is much, much longer than n, loop through n and run a binary
    search on m for each number.
    """

    duplicates = []


    def binary_search(m, num):

        begin = 0
        end = len(m) - 1

        while begin <= end:
            mid = (begin + end) / 2
            if num == m[mid]:
                return mid
            elif num > m[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return -1

    for num in n:
        if binary_search(m, num) != -1:
            duplicates.append(num)

    return duplicates
