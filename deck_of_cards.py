"""
deck_of_cards.py

This module defines classes for creating card games
"""

import random

class Card:
    """
    This represents a single card.
    Face Values: ace,king,queen,jack,10,9,8,7,6,5,4,3,2 and optionally joker
    Suite Values: hearts,clubs,diamonds,spades and optionally big and little (for jokers)
    """
    def __init__(self,suite,face):
        """Initializes a card"""
        self.suite = suite
        self.face = face

    def get_suite(self):
        """
        returns the suite of the card
        Suite Values: hearts,clubs,diamonds,spades and optionally big and little (for jokers)
        """
        return self.suite

    def get_face(self):
        """
        returns the face of the card
        Face Values: ace,king,queen,jack,10,9,8,7,6,5,4,3,2 and optionally joker
        """
        return self.face

class Deck:
    def __init__(self, include_jokers):
        """When include_jokers = True, both Big and Little Joker will be added to the deck"""
        suites = ["hearts", "diamonds", "spades", "clubs"]
        faces = ["ace", "king", "queen", "jack"]
        for num in range(2, 11):
            faces.append(str(num))
        # print(faces)
        deck = []
        for suite in suites[::]:
            for face in faces[::]:
                card = Card(suite,face)
                deck.append(card)
        if include_jokers:
            card = Card('big','joker')
            deck.append(card)
            card = Card('little','joker')
            deck.append(card)
        self.deck = deck

    def shuffle_Deck(self):
        """shuffleDeck will shuffle the deck via a randomized loop.  It will
         loop 7 times makes deck sufficiently random """
        for loops in range(1, 8):
            newDeck = []

            #split the deck into two even (as you can) piles.
            tempDeck1 = self.deck[0:len(self.deck)//2]
            tempDeck2 = self.deck[len(self.deck)//2:len(self.deck)]
            for i in range(0, len(self.deck)):
                if random.randint(1, 2) == 1:
                    if tempDeck1:
                        newDeck.append(tempDeck1.pop())
                    elif tempDeck2:
                        newDeck.append(tempDeck2.pop())
                else:
                    if tempDeck2:
                        newDeck.append(tempDeck2.pop())
                    elif tempDeck1:
                        newDeck.append(tempDeck1.pop())
            self.deck = newDeck.copy()

    def deal_card(self):
        """this will remove the first card from the deck and return the card"""
        return self.deck.pop(0)

    def to_list(self):
        the_list = []
        for card in self.deck:
            card_dict = {'suite': card.get_suite(),'face': card.get_face()}
            the_list.append(card_dict)
        return the_list

