"""
Grokking the Coding Interview: Max Sum Contiguous Subarry w/ Length K
By: Suryakiran Santhosh
12/8/2020
"""


def max_sub_array_of_size_k(k: int, arr: list[int]) -> int:
    max_sum = 0
    cur_sum = 0

    if len(arr) < k:
        return -1
    if len(arr) == k:
        return sum(arr)

    for i in range(len(arr)-k+1):
        cur_sum = sum(arr[i:i+k])
        max_sum = max(max_sum, cur_sum)
    return max_sum


def main():
    print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))  # 9
    print(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))  # 7


if __name__ == "__main__":
    main()
