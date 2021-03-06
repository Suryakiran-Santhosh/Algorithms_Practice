"""
Algorithm Design Practice 
By: Suryakiran Santhosh
University of California, Davis
February 5, 2021

--------------------PROMPT-----------------------------------
Most candidates cannot solve this interview problem:

Input: "aaaabbbcca"
Output: [("a", 4), ("b", 3), ("c", 2), ("a", 1)]

Write a function that converts the input to the output
I ask it in the screening interview and give it 25 minutes
How would you solve it?
"""


def charCount(input: str) -> list:
    ans = list()  # creates list for answer
    stack = list()
    ptr = 0  # keeps track of the algos progress along the input

    for i in input:
        if (len(stack) == 0) or (stack[0] == i):
            stack.append(i)
            ptr += 1
        else:
            ans.append((stack[0], len(stack)))
            stack.clear()
            stack.append(i)
            ptr += 1

        # edge case for the very last element
        if (ptr == (len(input))):
            ans.append((stack[0], len(stack)))

    return (ans)


def main():
    print(charCount("aaaabbbcca"))
    print(charCount("aaaabbbccaaaaa"))
    print(charCount("a"))


if __name__ == "__main__":
    main()
