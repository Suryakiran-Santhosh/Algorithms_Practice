"""
LeetCode # : Defange IP Address
By: Suryakiran Santhosh

Prompt:
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:
    Input: address = "1.1.1.1"
    Output: "1[.]1[.]1[.]1"

Example 2:
    Input: address = "255.100.50.0"
    Output: "255[.]100[.]50[.]0"

Constraints:
    The given address is a valid IPv4 address.
"""


def defangIPaddr(address: str) -> str:
    ans = ""
    for i in range(0, len(address), 1):
        if address[i] == ".":
            ans += str("[.]")
        else:
            ans += address[i]
    return ans


def main():
    print(defangIPaddr(address="1.1.1.1"))  # Output: "1[.]1[.]1[.]1"
    print(defangIPaddr(address="255.100.50.0"))  # Output: "255[.]100[.]50[.]0"


if __name__ == "__main__":
    main()
