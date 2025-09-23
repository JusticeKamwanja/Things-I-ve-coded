from random import choice

suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']

values = ['King', 'Queen', 'Jack'] + list(range(10, 1, -1)) + ['Ace']


def get_card():
    value = choice(values)
    suit = choice(suits)
    
    print(f'Your card is the {value} of {suit}.')
    
    
print('\n')
get_card()
print('\n')