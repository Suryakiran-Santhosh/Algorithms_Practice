"""
LeetCode #26: Duplicates from Sorted Array
By: Suryakiran Santhosh

Prompt:
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length. Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2]
    Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

Example 2:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4]
    Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.

Constraints:
    0 <= nums.length <= 3 * 104
    -104 <= nums[i] <= 104
    nums is sorted in ascending order.
"""


def removeDuplicates(nums: list[int]) -> int:
    if (len(nums) == 0) or (len(nums) == 1):
        return len(nums)
    else:
        uniques = set()
        i = 0
        end = len(nums)
        while i < end:
            if nums[i] in uniques:
                del nums[i]
                end -= 1
            else:
                uniques.add(nums[i])
                i += 1
        return len(nums)


def main():
    print(removeDuplicates(nums=[1, 1, 2]))  # Output: 2, nums = [1,2]
    print(removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # Output: 5, nums = [0,1,2,3,4]


if __name__ == "__main__":
    main()
