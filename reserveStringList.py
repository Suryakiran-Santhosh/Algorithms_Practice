"""
LeetCode #344: Reverse String
By: Suryakiran Santhosh

PROMPT:
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place w/ O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:
    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:
    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
"""


def reverseArrayOfStrings(s: list[str]) -> list:
    """
        Do not return anything, modify s in-place instead.
    """
    left = 0  # first index
    right = len(s) - 1  # last index

    while left < right:
        f = s[left]
        r = s[right]
        s[left] = r
        s[right] = f

        left += 1
        right -= 1

    return s


def main():
    print(reverseArrayOfStrings(s=["h", "e", "l", "l", "o"]))  # Output: ["o","l","l","e","h"]
    print(reverseArrayOfStrings(s=["H", "a", "n", "n", "a", "h"]))  # Output: ["h","a","n","n","a","H"]


if __name__ == "__main__":
    main()
