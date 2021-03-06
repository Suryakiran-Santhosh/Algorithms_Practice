"""
Leet Code: 485. Max Consecutive Ones
By: Suryakiran Santhosh
12/6/2020

--> passed all leet code test cases
"""


def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    counter = 0
    max_ones = 0
    for i in nums:
        if i == 1:
            counter += 1
            max_ones = max(counter, max_ones)
        else:
            counter = 0
    return max_ones
