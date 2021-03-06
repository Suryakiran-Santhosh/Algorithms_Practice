"""
Daily Byte #3

This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. 
A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, 
or only the first letter is capitalized.

Ex: Given the following strings...
    "USA", return true
    "Calvin", return true
    "compUter", return false
    "coding", return true
"""


def correctCapitalization(s: str) -> bool:
    if s == "":
        return True

    # 4 cases: 1.) all caps, 2.) first leter cap, 3.) no letters caps, 4.) improper capitalization
    firstLetter = False
    capCounter = 0

    if s[0].isupper():
        firstLetter = True
        capCounter += 1

    for i in range(1, len(s), 1):
        if s[i].isupper():
            capCounter += 1

    if (capCounter == 1 and firstLetter) or (capCounter == 0) or (capCounter == len(s)):
        return True
    else:
        return False

    """
    Time Complexity: O(n) bc each letter is checked once
    Space Complexity: O(1) bc only used two variables a boolean and an int which is ne gligible space
    """


def main():
    print(correctCapitalization(s="USA"))  # Output: true
    print(correctCapitalization(s="Calvin"))  # Output: true
    print(correctCapitalization(s="compUter"))  # Output: false
    print(correctCapitalization(s="coding"))  # Output: true


if __name__ == "__main__":
    main()
