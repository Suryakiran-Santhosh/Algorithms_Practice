"""
Leet Code: 11. Container With Most Water
By: Suryakiran Santhosh
12/6/2020

--> passed all leet code test cases
"""


def maxArea(height):
    area = 0
    start = 0
    end = len(height) - 1

    # optimize the while loop by disregarding area calculation in which the height
    # is not greater previous height values
    prev_start_height = 0
    prev_end_height = 0

    while start != end:
        if prev_start_height > height[start]:
            start += 1
            continue
        if prev_end_height > height[end]:
            end -= 1
            continue

        # area = width(delta index) * min(height)
        a = (end - start) * min(height[start], height[end])
        if area < a:  # checks if a is more feasible solution
            area = a

        if height[start] < height[end]:  # move pointer to right
            prev_start_height = height[start]
            start += 1
        else:  # move pointer to left
            prev_end_height = height[end]
            end -= 1

    return area


if __name__ == "__main__":
    print("test case start")
    print(maxArea([6, 4, 3, 1, 4, 6, 99, 62, 1, 2, 6]))  # 62
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
    print(maxArea([4, 3, 2, 1, 4]))  # 16
    print(maxArea([1, 1]))  # 1
    print(maxArea([1, 2, 1]))  # 2
    print(maxArea([1, 0, 0, 0, 0, 0, 0, 2, 2]))  # 8
    print("test case done")
