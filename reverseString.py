"""
Daily Byte: Reverse a String
By: Suryakiran Santhosh

Prompt: This question is asked by Google. 
Given a string, reverse all of its characters and return the resulting string.

Ex: Given the following strings...
    “Cat”, return “taC”
    “The Daily Byte”, return "etyB yliaD ehT”
    “civic”, return “civic”
"""


def reverseString(s: str) -> str:
    result = ""
    index = len(s) - 1  # pointer to the last element in the string
    while index >= 0:
        result += str(s[index])
        index -= 1
    return result


def main():
    print(reverseString("Cat"))  # Output: "taC"
    print(reverseString("The Daily Byte"))  # Output: "etyB yliaD ehT"
    print(reverseString("civic"))  # Output: "civic"


if __name__ == "__main__":
    main()
