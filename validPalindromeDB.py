"""
Daily Byte: Valid Palindrome
By: Suryakiran Santhosh

Prompt: This question is asked by Facebook. 
Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...
    "level", return true
    "algorithm", return false
    "A man, a plan, a canal: Panama.", return true
"""


def validPalindrome(s: str) -> bool:
    """
    two pointer: one front and one back of string, move towards the middle until all the letters in string have been processed
    """
    cleanS = ""

    # clean the string of all non alphabetical letters
    for i in range(0, len(s), 1):
        if s[i].isalpha():
            cleanS += str(s[i].lower())

    left = 0
    right = len(cleanS) - 1

    while left <= right:
        if (cleanS[left].isalpha() and cleanS[right].isalpha()):
            if (cleanS[left] != cleanS[right]):
                return False
        left += 1
        right -= 1
    return True


def main():
    print(validPalindrome("level"))  # Output: true
    print(validPalindrome("algorithm"))  # Output: false
    print(validPalindrome("A man, a plan, a canal: Panama."))  # Output: true


if __name__ == "__main__":
    main()
