#Bingo callout program
import random

#Bingo nickname array
BingoTerms = [["Kelly's Eye, Number one"],["One little duck, Number two"],["Cup of tea, Number three"],["Knock at the door, Number four"],["Man alive, Number five"],["Tom Mix, Number six"],["Lucky, Number seven"],["Garden gate, Number eight"],["Doctor's Orders, Number nine"],["David's Den, Number ten"]]

#stating nobody has had bingo before the game starts
Bingo = "n"

#While nobody has won
while "y" not in Bingo:
    #Generating random number less than the length of BingoTerms
    NumberGenerated = random.randint(0,(len(BingoTerms)-1))

    #Printing the nickname of the number
    print(BingoTerms[NumberGenerated])

    #Removing the number from the array
    del BingoTerms[NumberGenerated]

    #Checking if there has been a winner
    Bingo = input("Has anybody won?")
    print("\n")

    #If the array empties (So somebody must have won)
    if len(BingoTerms) == 0:
        Bingo = "y"
        print("You might want to check again")


