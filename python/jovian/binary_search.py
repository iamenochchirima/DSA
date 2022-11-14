def binary_search(cards, query):
    first, last = 0, len(cards)-1

    while first <= last:
        mid = (first + last)//2

        mid_num = cards[mid]

        if query == mid_num:
            return mid
        elif query < mid_num:
            last = mid-1
        else:
            first = mid+1
    return None

cards = [1, 2, 3, 4, 5, 6, 7, 8]
query = 7


result = binary_search(cards, query)

print(result)