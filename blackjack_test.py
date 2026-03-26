import unittest
from blackjack import isBlackJack, calcPoints
from deck_of_cards import Card

class Blackjack_test(unittest.TestCase):
    def test_isBlackJack_1(self):
        """Validates first card ACE, second card King is a blackjack"""
        card1 = Card("hearts","ace")
        card2 = Card("hearts","king")
        hand = (card1, card2)
        self.assertTrue(isBlackJack(hand))

    def test_isBlackJack_2(self):
        """Validates first card is jack, second card King is a ace"""
        card1 = Card("hearts","jack")
        card2 = Card("hearts","ace")
        hand = (card1, card2)
        self.assertTrue(isBlackJack(hand))

    def test_isBlackJack_3(self):
        """Validates first card is 5, second card is 5, third card is ace is NOT a blackjack"""
        card1 = Card("hearts","5")
        card2 = Card("clubs","5")
        card3 = Card("spades","ace")
        hand = (card1, card2, card3)
        self.assertFalse(isBlackJack(hand))

    def test_isBlackJack_4(self):
        """Validates first card is ace, second card is 5 is NOT a blackjack"""
        card1 = Card("hearts","ace")
        card2 = Card("clubs","5")
        hand = (card1, card2)
        self.assertFalse(isBlackJack(hand))

    def test_calc_points_1(self):
        """Validates  2, ACE, QUEEN returns 13"""
        card1 = Card("hearts","2")
        card2 = Card("clubs","ace")
        card3 = Card("hearts","queen")
        hand = (card1, card2, card3)
        self.assertEqual(13,calcPoints(hand))

    def test_calc_points_2(self):
        """Validates  2, ACE, ACE, QUEEN returns 14"""
        card1 = Card("hearts","2")
        card2 = Card("clubs","ace")
        card3 = Card("hearts","ace")
        card4 = Card("hearts", "queen")
        hand = (card1, card2, card3,card4)
        self.assertEqual(14,calcPoints(hand))

    def test_calc_points_3(self):
        """Validates  2, ACE, ACE, QUEEN, ACE returns 15"""
        card1 = Card("hearts", "2")
        card2 = Card("clubs", "ace")
        card3 = Card("hearts", "ace")
        card4 = Card("hearts", "queen")
        card5 = Card("diamonds","ace")
        hand = (card1, card2, card3, card4,card5)
        self.assertEqual(15, calcPoints(hand))

    def test_calc_points_3(self):
        """Validates  ACE, QUEEN returns 21"""
        card1 = Card("hearts", "ace")
        card2 = Card("clubs", "queen")
        hand = (card1, card2)
        self.assertEqual(21, calcPoints(hand))

    def test_calc_points_4(self):
        """Validates  3, KING. QUEEN returns 23"""
        card1 = Card("hearts", "3")
        card2 = Card("clubs", "king")
        card3 = Card("clubs", "queen")
        hand = (card1, card2, card3)
        self.assertEqual(23, calcPoints(hand))

    def test_calc_points_5(self):
        """Validates  KING, 3, ace, 5, 3 returns 22"""
        card1 = Card("hearts", "king")
        card2 = Card("clubs", "3")
        card3 = Card("clubs", "ace")
        card4 = Card("clubs", "5")
        card5 = Card("diamonds", "3")
        hand = (card1, card2, card3,card4,card5)
        self.assertEqual(22, calcPoints(hand))

if __name__ == '__main__':
    unittest.main()