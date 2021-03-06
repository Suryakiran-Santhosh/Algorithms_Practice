"""
MDSA Most Used Character in a String
By: Suryakiran Santhosh
"""


def mostUsedChar(s: str) -> str:
    charsInStr = dict()
    mostUsedLetter = ""
    numOfTimesUsed = 0

    s = s.rstrip(" ").lstrip(" ").lower()

    # goes through string and checks if letter is in hash else it adds it in the dictionary
    for letter in s:
        if letter.isalpha():
            if letter in charsInStr:
                charsInStr[letter] += 1
            else:
                charsInStr[letter] = 1

    # find the letter with the most occurrences
    for key, val in charsInStr.items():
        if numOfTimesUsed < val:
            mostUsedLetter = key
            numOfTimesUsed = val

    return mostUsedLetter


def main():
    print(mostUsedChar("aabbccc"))
    print(mostUsedChar("This is a common interview question"))  # i
    print(mostUsedChar("Prints the values to a stream, or to sys.stdout by default. Optional keyword arguments: \
        file: a file-like object (stream); defaults to the current sys.stdout. sep: string inserted between values, \
        default a space. end: string appended after the last value, default a newline. flush: whether to forcibly \
        flush the stream."))


if __name__ == "__main__":
    main()
