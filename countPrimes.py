"""
LeetCode 204: Count Primes
By: Suryakiran Santhosh

Prompt:
Count the number of prime numbers less than a non-negative number, n.

Example 1:
    Input: n = 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
    Input: n = 0
    Output: 0

Example 3:
    Input: n = 1
    Output: 0

Constraints: 0 <= n <= 5 * 106
"""


def countPrimes(n: int) -> int:
    # define an array of size n with all elements initialized to 1
    # 1 means prime
    table = [1] * n
    ans = 0

    # find all factors of a number and change the prime to composite in table
    for i in range(2, n):
        for j in range(2, n):
            index = i * j
            if index < len(table):
                if table[index] == 1:
                    table[index] = 0
            else:
                break

    # count all primes in table
    for i in range(2, n):
        if table[i] == 1:
            ans += 1

    return ans


def main():
    print(countPrimes(10))  # Output: 4
    print(countPrimes(0))  # Output: 0
    print(countPrimes(1))  # Output: 0
    print(countPrimes(100))


if __name__ == "__main__":
    main()
