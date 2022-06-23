############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
yourList = []
yourScore = 0
dealerList = []
endGame = False

def deal():
    """Deal 2 cards to the players"""
    for _ in range (2):
        yourList.append(random.choice(cards))
        dealerList.append(random.choice(cards))
    return yourList, dealerList

def yourDeal():
    """Ask for another card and deal a new one"""
    global yourList
    global yourScore
    global endGame
    while yourScore <=21:
        anotherCard = input("Type 'y' to get another card or type 'n' to pass: ")
        if anotherCard == "y":
            yourList.append(random.choice(cards))
            yourScore = sum(yourList)
            if yourScore > 21 and 11 in yourList:
                yourList[yourList.index(11)] = 1
                yourScore = sum(yourList)
            print(f"Your cards: {yourList}")
        elif anotherCard == 'n':
            return yourScore, yourList
        else:
            print ("Please, type a valid format")
    endGame = True
    print("You lose")
    return yourScore, endGame

def dealerDeal(dealerList, yourScore):
    """Add cards to dealer list until dealerScore>yourScore"""
    dealerScore = sum(dealerList)
    while dealerScore < yourScore:
        dealerList.append(random.choice(cards))
        dealerScore = sum(dealerList)

    print(f"Dealers cards: {dealerList} which is a score of {dealerScore}")
    if dealerScore > 21:
        print("You win")
    else:
        print("You lose")
    endGame = True
    return endGame

def play():
    """Runs the game"""
    global yourList
    global yourScore
    global dealerList
    global endGame
    yourList = []
    yourScore = 0
    dealerList = []

    print("Welcome to my first blackjack game!")
    deal()

    yourScore = sum(yourList)
    print(f"Your cards: {yourList} and your score is: {yourScore}")
    if yourScore == 21:
        print("Blackjack! You Win")
        endGame = True
    else:
        print(f"Dealers first card: {dealerList[0]}")
        yourDeal()
    if endGame == False:
        print(dealerList)
        if sum(dealerList)==21:
            print("Dealer's Blackjack, dealer win.")
        dealerDeal(dealerList, yourScore)

def askPlayAgain():
    """Ask for a new game"""
    playAgain = input("Do you want to play again? (Type 'y' or 'n'): ")
    while playAgain != 'y':
        if playAgain == 'n':
            return playAgain, print("Thanks for playing it!")
        print("Please, type a valid format")
        playAgain = input("Do you want to play again? (Type 'y' or 'n'): ")
    return playAgain

play()
playAgain = input("Do you want to play again? (Type 'y' or 'n'): ")
while playAgain == 'y':
    play()
    askPlayAgain()


