#BlackJack
import sys
from random import randint

#An Array to store all the suits
suits = ['Spade','Diamond','Club','Heart']

#An Array to store all the cards of a partiular suits
cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
cardNumber = {0 : 1, 1 : 2, 2 : 3, 3 : 4, 4 : 5, 5 : 6, 6 : 7, 7 : 8, 8 : 9, 9 : 10, 10 : 10, 11 : 10, 12 : 10}

#To keep a track of duplicate cards
inPlay = [False] * 52

userScore = 0
userCardCount = 0
dealerScore = 0
dealerCardCount = 0
stillPlaying = True
stillPlayingDealer = True


def gameOver():
    playAgain = raw_input("Do you want to play again? Y/N")
    playAgain = playAgain.lower()
    if(playAgain == "yes" or playAgain == "y"):
        play()
    else:
        sys.exit()

def userPlay():
    global stillPlaying
    while(stillPlaying == True):
        userMove = " "
        while(userMove != "H" and userMove != "S"):
            userMove = raw_input("Hit or Stand? H/S")
        if(userMove == "H"):
            while(generateCardUser() == False):
                #do nothing and call again
                print "  "
            print "Your current score is "+ str(userScore)
            if(userScore > 21):
                print "You are busted! Game Over"
                gameOver()
            userMove = " "

        elif(userMove == "S"):
            userMove = " "
            stillPlaying = False
            print "Your final score is " + str(userScore)
            print "Time for the dealer to play"

def dealerPlay():
    print "Dealer score is "+ str(dealerScore)
    if(dealerScore > 21):
        print "Dealer busted! You win!!"
        gameOver()
    global stillPlayingDealer
    while(stillPlayingDealer == True):
        dealerMove = " "
        while(dealerMove != "H" and dealerMove != "S"):
            dealerMove = raw_input("Hit or Stand? H/S")
        if(dealerMove == "H"):
            while(generateCardDealer() == False):
                #do nothing and call again
                print "  "
            print "Dealer current score is "+ str(dealerScore)
            if(dealerScore > 21):
                print "Dealer busted! You win!!"
                gameOver()
            dealerMove = " "

        elif(dealerMove == "S"):
            dealerMove = " "
            stillPlayingDealer = False
            print "Dealer's final score is " + str(dealerScore)



def generateCardUser():
    suitRandom = randint(0,3)
    cardRandom = randint(0,12)
    cardvalue = suitRandom*13 + cardRandom
    if(inPlay[cardvalue] == False):
        inPlay[cardvalue] = True
        global userScore
        global userCardCount
        userScore = userScore + cardNumber[cardRandom]
        userCardCount = userCardCount + 1
        print "Card generated is " + cards[cardRandom] + " of " + suits[suitRandom]
        return True
    else:
        return False

def generateCardDealer():
    suitRandom = randint(0,3)
    cardRandom = randint(0,12)
    cardvalue = suitRandom*13 + cardRandom
    if(inPlay[cardvalue] == False):
        inPlay[cardvalue] = True
        global dealerScore
        global dealerCardCount
        dealerScore = dealerScore + cardNumber[cardRandom]
        dealerCardCount = dealerCardCount + 1
        return True
    else:
        return False

def deal():
    while(userCardCount < 2):
        generateCardUser()
    if(userScore > 21):
        print "You are busted! Game Over"
        gameOver()
    else:
        print "Your score is "+ str(userScore)
        while(dealerCardCount < 2):
            generateCardDealer()

def play():
    #A boolean array to check if the card is in play or not
    inPlay = [False] * 52
    global userScore
    userScore = 0
    global userCardCount
    userCardCount = 0
    global dealerScore
    dealerScore = 0
    global dealerCardCount
    dealerCardCount = 0
    global stillPlaying
    stillPlaying = True
    global stillPlayingDealer
    stillPlayingDealer = True
    deal()
    userPlay()
    dealerPlay()
    if(dealerScore > userScore):
        print "Dealer wins"
        gameOver()
    else:
        print "You win"
        gameOver()

def main():
    play()

if __name__ == '__main__':
    main()
