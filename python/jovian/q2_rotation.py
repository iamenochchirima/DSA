"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a 
function to determine the minimum number of times the original sorted list was rotated to obtain the 
given list. Your function should have the worst-case complexity of O(log N), where N is the length of 
the list. You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 
9] 3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first 
element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 
7].

----------------------------------------------------------------------------------------------------

Input: A list of rotated sorted numbers
Output: the number of times the list was rotated

Examples of test cases:

1. A list of size 10 rotated 3 times.
2. A list of size 8 rotated 5 times.
3. A list that wasn't rotated at all.
4. A list that was rotated just once.
5. A list that was rotated n-1 times, where n is the size of the list.
6. A list that was rotated n times (do you get back the original list here?)
7. An empty list.
8. A list containing just one element.
(can you think of any more?)
"""

"""

Linear search solution:

def count_rotations(nums):

    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            return i
    return 0

list = [8, 0, 2, 3, 4, 5, 6, 7]

result = count_rotations(list)
print(result)

"""

def count_rotations(nums):

    #Set varieables for the first, last and mid values
    first = 0
    last = len(nums)-1

   

    #Run the loop as longs as the first number is bigger than the last, i.e as the list is rotated
    while first <= last:
        mid = (first+last)//2

        #if middle number is less than left then mid is the answer
        if mid > 0 and nums[mid]<nums[mid-1]:
            return mid
        elif nums[mid]<nums[last]:
            last = mid-1
        else:
            first = mid+1
    return 0
    
list = [6, 7, 8, 9, 10, 4, 5]

result = count_rotations(list)
print(result)