#Importing modules (time random and close program)
import random
import time
import sys

#creating array/list variable
Answers =["It is certain","Outlook good","You may rely on it","Ask again later","Concentrate and ask again","Reply hazy, try again","My reply is no","My sources say no"]
Answers_Yes_No =["Yes","No"]

#loop
loop = "on"
#getting name variable
Name = input("What is your name? ")
#printing text + name
print (("Thanks ") + Name + (" for purchasing the magic 8 ball"))
#asking for number of answers creating a integer variable
Number_Of_Answers = int(input("How many possible answers would you like there to be, 2 or 8? (2 are Yes/No) (type exit to quit) "))
#more of the loop
while loop == "on":
    #if statement to contol answer number
    if Number_Of_Answers == 2:
        #getting question ans setting as variable
        question = input("Ask the magic 8 ball a question: (type exit to quit) ")

        if question == "exit":
            sys.exit()
        #getting random answer from list
        Answer = random.choice(Answers_Yes_No)
        #printing text
        print("Shaking...")
        #Pause for added effect
        time.sleep(1)
        #printing answer (without apostrophies)
        print(''.join(Answer))
        #setting answer to nothing for repeat
        Answer= []
    #if statement to contol other answer number
    elif Number_Of_Answers == 8:                       
        #getting question ans setting as variable
        question = input("Ask the magic 8 ball a question: (type exit to quit) ")
        #getting random answer from list
        Answer = random.choice(Answers)
        #printing text
        print("Shaking...")
        #Pause for added effect
        time.sleep(1)
        #printing answer (without apostrophies)
        print(''.join(Answer))
        #setting answer to nothing for repeat
        Answer= []
    #if statement for if no answer given
    elif Number_Of_Answers == "exit":
        #end loop
        sys.exit()
