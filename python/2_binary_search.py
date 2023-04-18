def binary_search(items, target):
    first = 0
    last = len(items) - 1

    while first <= last:
        midpoint = (first+last)//2

        print("mid:", midpoint)
        print("first:", first, "last:", last)

        if items[midpoint] == target:
            return midpoint
        elif items[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print("Target found at:", index)
    else:
        print("Target not found in items")


numbers = range(1, 10000000)

result = binary_search(numbers, 9999998)

verify(result)