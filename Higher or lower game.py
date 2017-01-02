print("-\\\Welcome to the higher or lower array//-")
import random
packOfCards = []
aSuites = ["Hearts", "Clubs", "Spades", "Diamonds"]
aCards = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
#The card number (relating to the aCards array)
cardNumber = 1

#The suite number (relating to the aSuite array)
cardSuite = 0

High = False

#Getting it to loop forever
Continue = "1"
sGame= "0"
#Game menu
if "0" in sGame:
    #Generating the array and populating (4 lots of 13)
    for i in range(0,4): 
        for j in range(0,12):
            packOfCards.insert(0,(aCards[cardNumber] + " of " + aSuites[cardSuite]))
            #incrementing the card number
            cardNumber = (cardNumber + 1)
        #incrementing the suite number
        cardSuite = (cardSuite +1)
        #Resetting the card number for the next iteration
        cardNumber = 1

print("done")
for k in range(0,52):
    cardNumber = random.randint(0,(len(packOfCards)-1))
    firstcard= packOfCards[cardNumber]
    print(firstcard)
        
        #Removing the generated card
            
    del packOfCards[cardNumber]
    sGame= input("Higher Or Lower")
    if "h" in sGame.lower():
        High = True

    print(High)
        
