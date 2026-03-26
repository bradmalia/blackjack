import unittest
from deck_of_cards import Deck, Card

class DeckTest(unittest.TestCase):
    """tests for deck of cards"""

    def test_deck_size_no_jokers(self):
        """Validates there are 52 cards in the deck"""
        deck = Deck(include_jokers=False)
        cards = deck.to_list()
        self.assertEqual(52,len(cards))

    def test_deck_size_with_jokers(self):
        """Validates there are 54 cards in the deck"""
        deck = Deck(include_jokers=True)
        cards = deck.to_list()
        self.assertEqual(54, len(cards))
if __name__ == '__main__':
    unittest.main()