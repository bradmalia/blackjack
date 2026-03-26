import os
import math
from deck_of_cards import Card, Deck
import json

def calcPoints(hand):
    """Calculates the points of a hand"""
    points = 0
    ace_count = 0
    for card in hand:
        face = card.get_face()
        if face.lower() == 'ace':
            points += 11
            ace_count += 1
        elif face in {'king','queen','jack'}:
            points += 10
        elif face.isdigit():
            points += int(card.get_face())
    if points > 21:
        for i in range(ace_count):
            points -=10
            if points <= 21:
                break
    return points

# def printHand(owner, hand, hideCard):
#     """
#     Displays the hand in this format when hideCard = False - All cards shown
#     [Owner] Cards:
#       10 of Diamonds
#       9 of Diamonds
#     Total: 19
#
#     Displays hand in this format when HideCard = True - Hide second card
#     Dealer Cards:
#       Ace of Spades
#       ** Face Down **
#     Total: ?
#     """
#     print(f"{owner} Cards: ")
#     points = 0
#     card_count = 0
#     for card in hand:
#         card_count += 1
#         if hideCard and card_count == 2:
#             print("  ** Face Down **")
#         else:
#             print(f"  {card.get_face().title()} of {card.get_suite().title()}")
#
#     if hideCard:
#         points = '?'
#     else:
#         points = calcPoints(hand)
#     print(f"Total: {points}\n")
#
#     return points

def dealerPlay(hand, deck):
    """Dealer will build a hand that is at least 17 points"""
    while calcPoints(hand) < 17:
        print('Dealer gets a card...')
        hand.append(deck.deal_card())

def clear_screen():
    """clears the console screen"""
    if 'TERM' in os.environ:
        os.system('cls' if os.name == 'nt' else 'clear')

def isBlackJack(hand):
    """determines if a hand is a blackjack. Returns True or False"""
    isBlackJack = False
    if len(hand) == 2:
        hasAce = False
        hasTen = False
        for card in hand[:]:
            if 'ace' == card.get_face():
                hasAce = True
            if card.get_face() in ("10","jack","queen","king"):
                hasTen = True
        if hasAce and hasTen:
            isBlackJack = True
    return isBlackJack

def collectBet(playerBank):
    """
       Inputs a playerBank value and requests the player to enter a bet and validates value is correct
      Bet must be a valid integer between 1 and playerBank total
    """
    bet = 0
    bet = playerBank + 1
    validBet = False
    while not validBet:
        try:
            bet = int(input('Place your bet: '))
        except ValueError:
            bet = 0
        if bet > playerBank or bet <= 0:
            bet = playerBank + 1
            print('Invalid Bet...')
        else:
            playerBank -= bet
            validBet = True
    print(f'Bet: {bet} - Bank: {playerBank}\n')

    return bet

def dealHands(deck, playerHand, dealerHand):
    """
    Gives both player and dealer 2 cards.
    Player->Dealer->Player->Dealer
    """
    # print("Dealing cards...")
    playerHand.append(deck.deal_card())
    dealerHand.append(deck.deal_card())
    playerHand.append(deck.deal_card())
    dealerHand.append(deck.deal_card())

def do_gui(playerHand, dealerHand, hideDealer, playerBank, playerBet, previousBet=0):
    clear_screen()
    print("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*")
    print("|                 Blackjack v1.0                    |")
    print("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*")
    printString = '| Player Bank: '+str(playerBank)
    if previousBet != 0:
        printString = printString + ' | Previous Bet: ' + str(previousBet)
    elif playerBet:
        printString = printString + ' | Current Bet: '+str(playerBet)
    printString = printString.ljust(52,' ')+'|'
    print(printString)
    print("*---------------------------------------------------*")
    has_cards= False #used to handle when no cards have been delt yet.
    for i in range(0, max(len(playerHand),len(dealerHand))):
        printString = ''

        if i == 0:
            # print this line on first loop
            print("|   Dealer                |   Player                |")
        else:
            has_cards = True  #Validated that there are cards in player/dealer hand
        try:
            dealerCard = dealerHand[i]
            if i > 0 and hideDealer:
                printString = printString + '|     ???'
            else:
                printString = '|     ' + dealerCard.get_face().title() + ' of ' + dealerCard.get_suite().title()
        except IndexError:
            printString = '|'
        printString = printString.ljust(26,' ')
        try:
            playerCard = playerHand[i]
            printString = printString + '|     '+ playerCard.get_face().title()+' of '+playerCard.get_suite().title()
        except IndexError:
            printString = printString + "|"
        printString = printString.ljust(52, ' ')
        printString = printString + '|'
        print(printString)
    if has_cards:   #only print totals if player/dealer has cards
        print("|-------------------------+-------------------------|")
        if hideDealer:
            dealerPoints = '?'
        else:
            dealerPoints = str(calcPoints(dealerHand))
        playerPoints = str(calcPoints(playerHand))
        printString = '|   Total: '+dealerPoints
        printString = printString.ljust(26, ' ')
        printString = printString + '|   Total: '+playerPoints
        printString = printString.ljust(52, ' ')+'|'
        print(printString)
        print("*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\n")
    # print("\nHow would you like to proceed?")
    #choice = input("(H)it, (S)tay, s(P)lit, (D)ouble Down, (Q)uit:  ")
    # Max cards a player can possibly have without busting is 11.


if __name__ == '__main__':
    clear_screen()
    playerBank = 100
    keepGoing = True
    firstRun = True
    while keepGoing:
        # get a shuffled deck of cards without jokers
        deck = Deck(include_jokers=False)
        deck.shuffle_Deck()
        playerHand = []
        dealerHand = []
        bet = None
        if firstRun:
            do_gui(playerHand, dealerHand, True, playerBank, bet)
            firstRun = False
        #perform bet collection
        bet = collectBet(playerBank)
        clear_screen()
        #subtract the bet from the players bank
        playerBank -= bet

        #deal the Player and Dealer hands
        dealHands(deck, playerHand, dealerHand)

        #print both dealer and player hands, hide the dealers 2nd card.
        #printHand('Dealer', dealerHand, True)
        #printHand('Your', playerHand, False)
        do_gui(playerHand,dealerHand,True,playerBank,bet)
        #Start a game round
        gameOn = True
        while gameOn:
            print("\nHow would you like to proceed?")
            if playerBank - bet >= 0:
                choice = input("(H)it, (S)tay, s(P)lit, (D)ouble Down, (Q)uit:  ")
            else:
                choice = input("(H)it, (S)tay, s(P)lit, (Q)uit:  ")
            if choice.lower() == 'q':
                print('Thank you for playing!')
                keepGoing = False
                do_gui(playerHand, dealerHand, True, playerBank, None, bet)
                break
            elif choice.lower() == 'h':
                clear_screen()
                #printHand('Dealer', dealerHand, True)
                playerHand.append(deck.deal_card())
                do_gui(playerHand, dealerHand, True, playerBank, None, bet)
                if  calcPoints(playerHand)> 21:
                    print('Bust!!!  You lose!')
                    if playerBank == 0:
                        print("You're out of money!  Game over!")
                        keepGoing = False
                    break
            elif choice.lower() in ('s','d'):
                clear_screen()
                do_gui(playerHand, dealerHand, False, playerBank, None, bet)
                if choice.lower() == 'd':
                    # print('Dealing card...')
                    playerHand.append(deck.deal_card())
                    playerBank  -= bet
                    bet = bet * 2
                    #do_gui(playerHand, dealerHand, True, playerBank, None, bet)
                dealerPlay(dealerHand, deck)
                dealerPoints = calcPoints(dealerHand)
                if dealerPoints > 21:
                    if isBlackJack(playerHand):
                        do_gui(playerHand, dealerHand, False, playerBank, None, bet)
                        print('!!!!Blackjack!!!!')
                        playerBank += math.floor(bet * 2.5)
                    else:
                        playerBank += bet*2
                        do_gui(playerHand, dealerHand, False, playerBank, None, bet)
                        print('Dealer Busts!!! You Win!')
                    break
                playerPoints = calcPoints(playerHand)
                if playerPoints == 21:
                    if isBlackJack(playerHand):
                        playerBank += math.floor(bet*2.5)
                        do_gui(playerHand, dealerHand, False, playerBank, None, bet)
                        print('!!!!Blackjack!!!!')
                    else:
                        playerBank += bet*2
                        do_gui(playerHand, dealerHand, False, playerBank, None, bet)
                        print('You Win!!!')
                    break
                elif playerPoints > dealerPoints:
                    playerBank += bet * 2
                    do_gui(playerHand, dealerHand, False, playerBank, None, bet)
                    print('You Win!')
                    break
                elif playerPoints == dealerPoints:
                    playerBank += bet
                    do_gui(playerHand, dealerHand, False, playerBank, None, bet)
                    print('Push!')
                    break
                else:
                    do_gui(playerHand, dealerHand, False, playerBank, None, bet)
                    print('You Lose!!!')
                    if playerBank == 0:
                        print("You're out of money!  Game over!")
                        keepGoing = False
                    break


## BUG - dealer had 21, i had 22, and it said I won - failed to trigger bust
# Bank: 100
# Place your bet: 50
# Dealing cards...
#
# Dealer cards:
#   5 of Diamonds
#   **Hidden**
#
# Your Cards:
#   10 of Spades
#   2 of Clubs
# Total: 12
#
# How would you like to proceed?
# (H)it, (S)tay, s(P)lit, (D)ouble Down, (Q)uit:  d
# Dealing card...
# Dealer gets a card...
# Dealer gets a card...
# Dealer Cards:
#   5 of Diamonds
#   2 of Hearts
#   4 of Spades
#   10 of Hearts
# Total: 21
# Your Cards:
#   10 of Spades
#   2 of Clubs
#   Queen of Hearts
# Total: 22
# You Win!
# Bank: 200
# Place your bet:

# BUG - I think if both dealer and player have 21 and niether have blackjack, it incorrectly gives it to player.  it should be a push

# BUG - Performed a double down and it didn't display my cards
# How would you like to proceed?
# (H)it, (S)tay, s(P)lit, (D)ouble Down, (Q)uit:  d
# Dealing card...
# Dealer gets a card...
# Dealer gets a card...
# Dealer Cards:
#   6 of Clubs
#   7 of Diamonds
#   2 of Hearts
#   Jack of Hearts
# Total: 25
# Dealer Busts!!! You Win!
# Bank: 285
# Place your bet:

#BUG - You should only be able to double down on the first hit

#BUG - i busted on a double down and dealer played and also busted
# and it incorrectly gave me the win.
# *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
# |                 Blackjack v1.0                    |
# *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
# | Player Bank: 202 | Previous Bet: 2                |
# *---------------------------------------------------*
# |   Dealer                |   Player                |
# |     Ace of Diamonds     |     4 of Spades         |
# |     4 of Diamonds       |     Jack of Spades      |
# |     10 of Hearts        |     King of Clubs       |
# |     9 of Hearts         |                         |
# |-------------------------+-------------------------|
# |   Total: 24             |   Total: 24             |
# *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
#
# Dealer Busts!!! You Win!
# Place your bet:
#
#BUG I got a blackjack and it didn't display my winnings on the page, but it did on the next
