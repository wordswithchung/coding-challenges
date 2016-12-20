


def two_sum_v2(nums, target):
    """Given an array of integers, return indices of the two numbers such that
    they add up to a specific target.

    You may assume that each input would have exactly one solution.

        >>> two_sum([3, 29, 8, 1], 9)
        [2, 3]

        >>> two_sum([1, 2, 3, 4], 5)
        [0, 3]

        >>> two_sum([0, 1, 2, 0], 0)
        [0, 3]
    """

    # passing through the list only once, but still searching
    # only ever-so-slightly more efficient than the previous solution
    # there must be a better answer!

    for num in nums:
        other_half = target - num
        if other_half in nums:
            return [num.index(), other_half.index()]


def two_sum(nums, target):
    """Given an array of integers, return indices of the two numbers such that
    they add up to a specific target.

    You may assume that each input would have exactly one solution.

    https://leetcode.com/problems/two-sum/

        >>> two_sum([3, 29, 8, 1], 9)
        [2, 3]

        >>> two_sum([1, 2, 3, 4], 5)
        [0, 3]

        >>> two_sum([0, 1, 2, 0], 0)
        [0, 3]
    """

    # the O(n^2) solution; so not ideal :(

    for num in nums:
        for i in nums[nums.index(num) + 1:]:
            if num + i == target:
                return [nums.index(num), nums.index(i)]
