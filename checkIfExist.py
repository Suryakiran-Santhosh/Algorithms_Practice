"""
LeetCode # 1376 Check If N and Its Double Exist
By: Suryakiran Santhosh

Prompt:
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M). More formally check if there exists two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:
    Input: arr = [10,2,5,3]
    Output: true
    Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:
    Input: arr = [7,1,14,11]
    Output: true
    Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example 3:
    Input: arr = [3,1,7,11]
    Output: false
    Explanation: In this case does not exist N and M, such that N = 2 * M.

Constraints:
    2 <= arr.length <= 500
    -10^3 <= arr[i] <= 10^3
"""


def checkIfExist(arr: list[int]) -> bool:
    # Brute Force Approach: Nested For Loop
    # for i in range(0, len(arr)):
    #    for j in range(0, len(arr)):
    #        if i != j and arr[j] * 2 == arr[i]:
    #            return True
    # return False

    # Set Method
    # loop through array and check if the double of the element is in the set
    # if it is return True else return False
    if (len(arr) < 2):
        return False

    values = set()
    for i in range(len(arr)):
        if (arr[i] * 2 in values) or (arr[i] / 2 in values):
            return True
        else:
            values.add(arr[i])
    return False


def main():
    print(checkIfExist(arr=[10, 2, 5, 3]))  # Output: True
    print(checkIfExist(arr=[7, 1, 14, 11]))  # Output: True
    print(checkIfExist(arr=[3, 1, 7, 11]))  # Output: False
    print(checkIfExist(arr=[-2, 0, 10, -19, 4, 6, -8]))  # Output: False


if __name__ == "__main__":
    main()
