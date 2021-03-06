"""
LeetCode #67: Add Binary
By: Suryakiran Santhosh

Prompt:
Given two binary strings a and b, return their sum as a binary string.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

Constraints:
    1 <= a.length, b.length <= 104
    a and b consist only of '0' or '1' characters.
    Each string does not contain leading zeros except for the zero itself.
"""


def addBinary(a: str, b: str) -> str:
    if ((len(a) == 0) or (len(b) == 0)):  # edge case
        return ""

    val1 = binToInt(a)
    val2 = binToInt(b)
    intSum = val1 + val2
    binResult = bin(intSum)
    return binResult.lstrip("0b")


def binToInt(a: str) -> int:
    num = 0
    revA = a[::-1]
    for i in range(0, len(a)):
        x = int(revA[i]) * (2 ** i)
        num += x
    return num


def main():
    print(addBinary(a="11", b="1"))  # Output: "100"
    print(addBinary(a="1010", b="1011"))  # Output: "10101"


if __name__ == "__main__":
    main()
