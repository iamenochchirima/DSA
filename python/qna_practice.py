"""
Qn: Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
 and lays them out face down in a sequence on a table. She challenges Bob to pick out the card 
 containing a given number by turning over as few cards as possible. Write a function to help Bob 
 locate the card.
"""

def locate_card(cards, query):
    pass

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7
output = 3

result = locate_card(cards, query)
print(result)

result == output

test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}

locate_card() 