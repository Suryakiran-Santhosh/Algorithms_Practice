"""
Leet Code: 7.Reversing an Integer
By: Suryakiran Santhosh
12/8/2020
"""


def reverse(x: int) -> int:
    str_x = str(x)
    chars = len(str_x)
    if str_x[0] == "-":
        str_x = str_x.lstrip("-")
        rev = str_x[::-1]
        final = "-" + rev
        val = int(final)
        if val < -(2**31):
            return 0
        else:
            return val
    else:
        val = int(str_x[::-1])
        if val > (2**31)-1:
            return 0
        else:
            return val


def main():
    print(reverse(123))  # 321
    print(reverse(-123))  # -321
    print(reverse(120))  # 21
    print(reverse(0))  # 0


if __name__ == "__main__":
    main()
