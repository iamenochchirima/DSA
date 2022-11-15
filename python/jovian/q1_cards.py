"""
Qn: Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
 and lays them out face down in a sequence on a table. She challenges Bob to pick out the card 
 containing a given number by turning over as few cards as possible. Write a function to help Bob 
 locate the card.
"""

def locate_card(cards, query):
    
    # Create a variable with position 0
    position = 0

    print("cards: ", cards)
    print("query: ", query)

    #Set up a while loop for repetion
    while position < len(cards):

        print("position: ", position)
        #Check if the card at the position matches the query
        if cards[position] == query:
            return position
        
        # Increase the position by one.
        position += 1

        if position == len(cards):
            return None

tests = ({
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 0
    },
    'output': 7
})

result = locate_card(**tests['input']) == tests['output']

print(result)
