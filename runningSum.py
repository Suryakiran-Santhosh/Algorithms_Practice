"""
LeetCode #1480: Running Sum of 1d Array
By: Suryakiran Santhosh

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running  sum of nums.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [1,3,6,10]
    Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
    Input: nums = [1,1,1,1,1]
    Output: [1,2,3,4,5]
    Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
    Input: nums = [3,1,2,10,1]
    Output: [3,4,6,16,17]
 
Constraints:
    1 <= nums.length <= 1000
    -10^6 <= nums[i] <= 10^6
"""


def runningSum(nums: list[int]) -> list[int]:
    rSum = []
    rSum.append(nums[0])  # first element has a sum of itself
    for i in range(1, len(nums)):
        rSum.append(rSum[len(rSum) - 1] + nums[i])
    return rSum

    # time complexity is O(n) b/c each element is accessed once
    # space complexity is O(n) b/c the rSum array will have n new elements


def main():
    print(runningSum(nums=[1, 2, 3, 4]))  # Output: [1,3,6,10]
    print(runningSum(nums=[1, 1, 1, 1, 1]))  # Output: [1,2,3,4,5]
    print(runningSum(nums=[3, 1, 2, 10, 1]))  # Output: [3,4,6,16,17]


if __name__ == "__main__":
    main()
