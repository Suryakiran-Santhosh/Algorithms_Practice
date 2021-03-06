"""
LeetCode Question
By: Suryakiran Santhosh

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""


def sortedSquares(nums: list[int]) -> list[int]:
    """
    # Initial Approaches:
    # square all elements and then sort, Time: O(nlogn) Space: O(n)
    for i in range(len(nums)):  # linear time because length of array is n
        nums[i] = nums[i] ** 2
    return sorted(nums)  # average sort time is O(nlogn)
    """

    # Two Pointer Technique: check if left or right is bigger then assign to a list
    ans = [0] * len(nums)  # stores the squared values
    leftPtr = 0
    rightPtr = len(nums) - 1
    index = len(nums) - 1

    # going through all the elements in the array takes linear time O(n)
    while leftPtr <= rightPtr:
        if (abs(nums[leftPtr]) < abs(nums[rightPtr])) or (abs(nums[leftPtr]) == abs(nums[rightPtr])):
            ans[index] = nums[rightPtr] ** 2
            rightPtr -= 1
            index -= 1
        elif (abs(nums[leftPtr]) > abs(nums[rightPtr])):
            ans[index] = nums[leftPtr] ** 2
            leftPtr += 1
            index -= 1
    return ans


def main():
    print(sortedSquares([-7, -3, 2, 3, 11]))  # Output: [4,9,9,49,121]
    print(sortedSquares([-4, -1, 0, 3, 10]))  # Output: [0,1,9,16,100]


if __name__ == "__main__":
    main()
