"""
LeetCode Remove Elements Question
By: Suryakiran Santhosh
"""


def removeElement(nums: list[int], val: int):
    if val not in nums:
        return len(nums)
    i = 0
    while i < len(nums):
        if nums[i] == val:
            del nums[i]
        else:
            i += 1
    return len(nums)


def main():
    print(removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))  # [0,1,4,0,3]


if __name__ == "__main__":
    main()
