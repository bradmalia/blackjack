"""
player.py

This module defines classes for a player
"""


class Player:
    """
    This represents a single card.
    Face Values: ace,king,queen,jack,10,9,8,7,6,5,4,3,2 and optionally joker
    Suite Values: hearts,clubs,diamonds,spades and optionally big and little (for jokers)
    """
    def __init__(self,hand,bank):
        """Initializes a player"""
        self.hand = hand
        self.bank = bank
        self.bet = 0

    def get_hand(self):
        """
        returns hand of the player
        """
        return self.hand

    def get_bank(self):
        """
        returns an int amount of the bank
        """
        return self.bank


