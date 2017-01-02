#Creating pack of cards
import random
packOfCards = []
aSuites = ["Hearts", "Clubs", "Spades", "Diamonds"]
aCards = ["Blank", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
#The card number (relating to the aCards array)
cardNumber = 1

#The suite number (relating to the aSuite array)
cardSuite = 0

#Getting it to loop forever
Continue = "1"
sGame= "0"
#Game menu
if "0" in sGame:
    #Generating the array and populating (4 lots of 13)
    for i in range(0,4): 
        for j in range(0,13):
            packOfCards.insert(0,(aCards[cardNumber] + " of " + aSuites[cardSuite]))
            #incrementing the card number
            cardNumber = (cardNumber + 1)
        #incrementing the suite number
        cardSuite = (cardSuite +1)
        #Resetting the card number for the next iteration
        cardNumber = 1
    #asking what game is wanted
    sGame= input("What would you like to play? 21 game [1], random card game [2]")

while "1" in Continue:
    #Game menu
    if "0" in sGame:
        #Resetting the array and populating (4 lots of 13)
        packOfCards = []
        cardNumber = 1
        cardSuite = 0
        for i in range(0,4): 
            for j in range(0,13):
                packOfCards.insert(0,(aCards[cardNumber] + " of " + aSuites[cardSuite]))
                #incrementing the card number
                cardNumber = (cardNumber + 1)
            #incrementing the suite number
            cardSuite = (cardSuite +1)
            #Resetting the card number for the next iteration
            cardNumber = 1
        #asking what game is wanted
        sGame= input("What would you like to play? 21 game [1], random card game [2]")
        
    #21 Game
    while "1" in sGame:
        print("-\\\Welcome to 21//-")
        #Total number reset
        CardTotal= 0
        
        #Card generator
        cardNumber1= random.randint(1,13)
        cardNumber2= random.randint(1,13)

        #Card name selector
        firstcard= aCards[cardNumber1]
        secondcard= aCards[cardNumber2]

        #Ignoring picture card values
        if int(cardNumber1) > 9.5:
            cardNumber1= 10
        if int(cardNumber2) > 9.5:
            cardNumber2= 10
        
        #Card total addition
        CardTotal= CardTotal + cardNumber1 + cardNumber2

        #number of cards given
        numberOfCards= 2
        #Result printing
        print("you got the",firstcard ,"and the" , secondcard)
        print(CardTotal)
        
        #Whether a new card should be dealt
        Stick= input("Would you like another card?")

            
        while ("y" or "Y") in Stick:
            #Generating third card and naming
            cardNumber3 = random.randint(1,13)
            thirdcard= aCards[cardNumber3]

            #number of cards gicen
            numberOfCards= numberOfCards + 1

            #Card total addition
            if int(cardNumber3) > 9.5:
                cardNumber3= 10
                
            CardTotal= CardTotal + cardNumber3 

            #Result printing
            print("you got the",thirdcard)
            print(CardTotal)
            Stick= input("Would you like another card?")

        #If no new card needed
        else:
            #resetting dealer total for each game cycle
            DealerTotal= 0
            
            #Generating Dealer cards
            DealerNumber1= random.randint(1,13)
            DealerNumber2= random.randint(1,13)
            DealerNumber3= 0
            Dealercard1= aCards[DealerNumber1]
            Dealercard2= aCards[DealerNumber2]
            
            if int(DealerNumber1) > 9.5:
                DealerNumber1= 10
            if int(DealerNumber2) > 9.5:
                DealerNumber2= 10
                    
            DealerTotal= DealerTotal + DealerNumber1 + DealerNumber2
            while DealerTotal < 15:
                DealerNumber3= random.randint(1,13)
                DealerTotal= DealerTotal + DealerNumber3
            
        
            print("The dealer got a total of", DealerTotal)
           
            #Stating whether bust or not
            if CardTotal >21:
                print("You went bust!!!")
                sGame= input("Would you like to play again? [1] or would you like to play another game?[0]")

            #Stating whether user wins
            elif numberOfCards > 4:
                print("You got a 5 card charlie, You win!")
                sGame= input("Would you like to play again? [1] or would you like to play another game?[0]")
            else:
                if CardTotal > DealerTotal:
                    print("You win")
                    sGame= input("Would you like to play again? [1] or would you like to play another game?[0]")

                else:
                    print("you lose")
                    sGame= input("Would you like to play again? [1] or would you like to play another game?[0]")
        
    #Generating
    while "2" in sGame:
        print("-\\\Welcome to the random card game//-")
        for k in range(0,52):
            if "2" in sGame:
                cardNumber = random.randint(0,(len(packOfCards)-1))
                firstcard= packOfCards[cardNumber]
                print(firstcard)
        
                #Removing the generated card
            
                del packOfCards[cardNumber]
                sGame= input("Would you like another card? yes[1], no [0]")
                if "1" in sGame:
                    sGame= "2"
                else:
                    sGame= "0"

        
        #If nothing in deck array
        else:
            print("That's all the cards in the deck")
            sGame= "0"
