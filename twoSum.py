"""
LeetCode 1: Two Sum
By: Suryakiran Santhosh

Prompt:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

Constraints:
2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


def twoSum(nums: list[int], target: int) -> list[int]:
    table = dict()  # key: difference from target, value: index of second term
    for i in range(0, len(nums)):
        diff = target - nums[i]  # value to check in table for
        if (diff in table.keys()):  # checks to see if diff is in table
            return ([i, table.get(diff)])
        else:
            table[nums[i]] = i


def main():
    print(sorted(twoSum(nums=[2, 7, 11, 15], target=9)))  # Output: [0, 1]
    print(sorted(twoSum(nums=[3, 2, 4], target=6)))  # Output: [1, 2]
    print(sorted(twoSum(nums=[3, 3], target=6)))  # Output: [0, 1]


if __name__ == "__main__":
    main()
