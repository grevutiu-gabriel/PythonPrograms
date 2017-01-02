#DnD dice sim
import random
import time


#Defining the  dice subroutine
def Dice(diceside):
    #generating random number between 1 and dice sides
    numberRolled= random.randint(1,int(diceside))

    #returning the number rolled
    return numberRolled

#Defining the character subroutine
def Character(characterName):
    #Generating strength
    strength = str(round(10+ (Dice(12)/Dice(4))))

    #generating skill
    skill = str(round(10+ (Dice(12)/Dice(4))))

    #Opening text file and writing to it
    text_file = open("DnD.txt", "a")
    
    text_file.write(characterName)
    text_file.write("\n")
    text_file.write("With a mighty strength of ")
    text_file.write(strength)
    text_file.write("\n")
    text_file.write("With a skill of ")
    text_file.write(skill)
    text_file.write("\n")
    text_file.write("\n")
    text_file.close()

    print("Saved to DnD.txt\n")

#Defining the combat subroutine
def battle(char1Str, char2Str):
        notDead = "1"
        while "1" in notDead:
            #Calculating Strength modifier
            strengthmod = int((max(char1Str, char2Str) - min(char1Str, char2Str))/5)
            #rolling a dice for each player
            player1Dice = Dice(6)
            player2Dice = Dice(6)

            #Stopping the immortals
            if strengthmod == 0:
                strengthmod= Dice(6)

            #If player 1 rolls higher than player 2
            if player1Dice > player2Dice:
                char2Str = int(char2Str - strengthmod)
                print("fwoosh, Player 1 deals ",strengthmod , "damage to Player 2\n")
                time.sleep(0.5)
                print("Player 2 has", char2Str, "health left\n")

            #If player 2 rolls higher than player 1
            if player2Dice > player1Dice:
                char1Str = int(char1Str - strengthmod)
                print("Schwing , Player 2 deals ",strengthmod , "damage to Player 1\n")
                time.sleep(0.5)
                print("Player 1 has", char1Str, "health left\n")


            #Checking if dead
            if char1Str <= 0:
                notDead = "2"
                

            if char2Str <= 0:
                notDead = "3"
                

        if "2" in notDead:
            return("player 2 wins")

        if "3" in notDead:
            return("player 1 wins")
        
    

#Choosing what subprogram to run
sJob = str(input("What would you like to do?\n Character trait generation [1] Dice rolling [2] Battle Sim [3]\n"))

#Making it forever check what sumbroutine to run
Continue = 1

while Continue == 1:
    while not (("1" in sJob) or ("2" in sJob)or ("3" in sJob)):
        sJob = input("That's not a valid choice, please try again.\n Character trait generation [1] Dice rolling [2] Battle Sim [3]\n")

    #Character generagtor
    while "1" in sJob:
        #Getting character name from user
        characterName = input("What would you like your character's name to be?")
        Character(characterName)

        sJob = input("Would you like another service?\n Character trait generation [1] Dice rolling [2] Battle Sim [3]\n")
        


    #Dice sim
    while "2" in sJob:
        #Defining the number of sides desired  
        diceside = input("How many sides do you want the dice to have?")

        #printing the result
        print(Dice(diceside))
        
        sJob = input("Would you like another service?\n Character trait generation [1] Dice rolling [2] Battle Sim [3]\n")

    #Battle sim
    while "3" in sJob:
        #Getting the strength of the players characters
        char1Str = int(input("What is the strength of the first character?"))
        char2Str = int(input("What is the strength of the second character?"))
        #Running the subroutine
        print(battle(char1Str,char2Str))
        
        sJob = input("\nWould you like another service?\n Character trait generation [1] Dice rolling [2] Battle Sim [3]\n")
