"""
LeetCode #58 Length of Last Word
By: Suryakiran Santhosh

Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0. Word is a maximal substring consisting of non-space characters only.

Example 1:
    Input: s = "Hello World"
    Output: 5

Example 2:
    Input: s = " "
    Output: 0
 
Constraints:
    1 <= s.length <= 104
    s consists of only English letters and spaces ' '
"""


def lengthOfLastWord(s):
    lastWord = ""
    s = s.lstrip(" ").rstrip(" ")  # remove spaces from left and right of the string

    if len(s) == 0:
        return 0
    
    if " " not in s:
        return len(s)

    # from the end of the string move using a pointer iterate backwards until a space
    for letter in range(len(s) - 1, 0, -1):
        if not s[letter].isspace():
            lastWord += str(s[letter])
        else:
            break
    
    return len(lastWord)


def main():
    print(lengthOfLastWord(s="Hello World"))  # Output: 5
    print(lengthOfLastWord(s="a "))  # Output: 1
    print(lengthOfLastWord(s=" "))  # Output: 0
    print(lengthOfLastWord(s="        "))  # Output: 0



if __name__ == "__main__":
    main()