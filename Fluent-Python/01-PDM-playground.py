# Best way to use this files is to run/write each part in python REPL, or even you can use Ipython
# if you want to have a REPL with same variables and values as the file and test thing out
# ipython -i file_name OR python -i file_name
# Python Data Model --> Enable you to create your own object and use it in a Pythonic way
x = "hello world"
# Pythonic way
len(x) # print 11
# What Interpreter actually doing when running len
x.__len__() # print 11

y = [1, 2, 3]
# Pythonic
y[1] # print 2
# Magic Method, dunder method, double underscore method
y.__getitem__(1) # print 2

# No error cause z is a special data type that is similar to dict --> set
z = {"a", "b", "c"}
# Pythonic
type(z)
# Dunder method
z.__class__()
# To create an empty set you need to call its function
z = set()
set.__init__(z)

z = {"a":1, "b":2, "c":3}
# Pythonic way: obj[key] --> value
z["a"]
# What interpreter sees
z.__getitem__("a")

# create container data type
import collections

# namedtuple --> build classes of objects that are just bundles of attributes with no custome methods
# easy way to create a class
Card = collections.namedtuple('Card', ['rank', 'suit'])
# The one line above equal to

class Card_with_no_collections:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "Card(rank="+str(self.rank)+", suit="+str(self.suit)+")"


class FrenchDeck:
    # class variables
    # list comprehension and then adding cast of "JQKA" to list to it
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split(' ')

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')
# test in REPL
beer_card

deck = FrenchDeck()
# because you created your own len function you can use it this way:
len(deck) # print 52
# or
deck.__len__() # print 52
# if you didn't created your len function you will get an error
# to see the __getitem__ effect check this out
deck[0]
deck[-1]
# or you can write it in a bad way, not pythonic
deck.__getitem__(0)
deck.__getitem__(-1)

# function to choose a random card
from random import choice
# choose a card from a deck randomly
choice(deck)
# we only implemented the __getitem__ but now we can even use slicing
deck[10:12]
deck[6:13:2]
# You can even use reversed on deck an iterate over it
# I want to limit it to only 5 print
count = 0
for card in deck:
    print(card)
    count += 1
    if count > 5:
        break
# reinitialize count
count = 0
for card in reversed(deck):
    print(card)
    count += 1
    if count > 5:
        break

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(f"score of {card} is {spades_high(card)}")
