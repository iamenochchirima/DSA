"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), where N is the length of the list. You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].
"""

# With linear search

# def rotated_list(items):

#     for i in range(0, len(items)):
#         if items[i] < items[i-1] and i > 0:
#             return i
#     return None

# items = [1,2,3,4]

# results = rotated_list(items)

# print(results)

# def rotated_list2(items):
#     position = 0

#     while position < len(items):
#         if items[position] < items[position-1] and position > 0:
#             return position
#         position += 1
#     return 0

# items = [5,6,1,2,3,4]

# results = rotated_list2(items)

# print(results)

# With binary search

def find_rotations(nums):

    first = 0
    last = len(nums)-1 

    while nums[first] > nums[last]:
        mid = (first + last)//2
        mid_num = nums[mid]

        if mid > 0 and mid_num < nums[mid-1]:
            return mid
        elif mid_num < nums[last]:
            last = mid
        else:
            first = mid
    return 0 

items = [3,4,5,6,7,8,9,1,2]

results = find_rotations(items)

print(results)      


