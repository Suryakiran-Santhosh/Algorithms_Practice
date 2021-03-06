"""
LeetCode #796: Rotate String
By: Suryakiran Santhosh

PROMPT:
We are given two strings, A and B. A shift on A consists of taking string A and moving the leftmost character to the rightmost position.
For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
    Input: A = 'abcde', B = 'cdeab'
    Output: true

Example 2:
    Input: A = 'abcde', B = 'abced'
    Output: false

Note: A and B will have length at most 100.
"""


from random import randint
from string import ascii_lowercase


def rotateString(A: str, B: str) -> bool:
    if len(A) != len(B):
        return False
    elif A == "" and B == "":
        return True
    else:
        for i in range(0, len(A), 1):
            left = A[0]
            A = A[1::1]
            A += str(left)
            if A == B:
                return True
    return False
    # Time Complexity: O(n^2), Knuth Morris Algorithm or rolling hash algorithm would make it O(N)
    # Space Complexity: O(1) because not allocating extra space just removing and adding to the input string


def main():
    print(rotateString(A='abcde', B='cdeab'))  # Output: true
    print(rotateString(A='abcde', B='abced'))  # Output: false
    print(rotateString(A="bbbacddceeb", B="ceebbbbacdd"))  # Output: true

    # bigger string test case
    alphabet = ascii_lowercase   # string that holds all the letters in the alphabet
    sizeOfString = 1000000
    testCaseWordA = ""
    testCaseWordB = ""
    for i in range(sizeOfString):
        testCaseWordA += str(alphabet[randint(0, 25)])
        testCaseWordB += str(alphabet[randint(0, 25)])

    print(rotateString(A=testCaseWordA, B=testCaseWordB))


if __name__ == "__main__":
    main()
