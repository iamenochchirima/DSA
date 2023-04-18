def linear_search(cards, target):
    """
    Returns the index position of the target if found, else return none
    """

    for i in range(0, len(cards)):
        if cards[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found at:", index)
    else:
        print("Target not found in cards")

numbers = range(0)

result = linear_search(numbers, 7)

verify(result)


def locate_card(cards, query):

    position = 0

    while True:

        if cards[position] == query:
            return position
        
        position += 1

        if position == len(cards):
            return -1
        
cardss = [13, 11, 10, 7, 4, 3, 1, 0]
querys = 1

