#Dice Game
import random
iTotalPoints= 0
sWantToPlay= input(str.lower("would you like to play?"))
while "y" or "Y" in sWantToPlay:
    #Reset total
    iTotal= 0
    #Number of dice
    iDifficulty= int(input("how many dice would you like to play with?"))
    iHighestNumber= iDifficulty * 6

    #User guess
    t = "choose a number between", str(iDifficulty), "and", str(iHighestNumber)
    
    iUserGuess= input(t)

    
    #Dice number generation
    for x in range(0,iDifficulty):
        iDice= random.randint(1,6)
        iTotal= int(iTotal + iDice)


    #Result
    print("The dices say", iTotal)

    #Accuracy
    iAccuracy= (int(iTotal) - int(iUserGuess))

    if iAccuracy < 0:
        iAccuracy= -(iAccuracy)
              
    print("You were", iAccuracy, "Away")
    if -(iDifficulty *2)< iAccuracy <(iDifficulty *2):
        if -(iDifficulty + 0.1)< iAccuracy <(iDifficulty + 0.1):
            if iAccuracy == 0:
                print("Perfection, 100 points")
                iTotalPoints= iTotalPoints + 100
            else:
                print("Well done, 10 points")
                iTotalPoints= iTotalPoints + 10
        

        else:
            print("close, 5 points")
            iTotalPoints= iTotalPoints + 5

    else:
        print("Bad luck, no points for you")

    
    print("your total points are", iTotalPoints)

    sWantToPlay= input("would you like to play again?")
else:
    print("speak now or forever hold your peace")
