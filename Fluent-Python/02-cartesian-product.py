colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

suits = ['♣', '♦', '♥', '♠']
courts = ['A', 'K', 'Q', 'J']
court_cards = [(court, suit) for court in courts for suit in suits]

# more readable
court_cards = [(court, suit) for court in courts
                             for suit in suits]
# Understanding how it works
for court in courts:
    for suit in suits:
        print(court, suit)

from pprint import pprint
pprint(court_cards)

