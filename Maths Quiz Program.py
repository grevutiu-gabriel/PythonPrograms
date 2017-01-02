#Maths quiz
import random
Name = input("What is your name?")
Operations= ["*","+","-"]
CorrectAnswer= []
TotalCorrect = 0
#Creating 10 questions and checking
for x in range(0,10):
    #Generating Numbers and operation
    Number1= random.randint(0,12)
    Number2= random.randint(0,12)
    OperationNo= random.randint(0,2)
    #Printing equation
    print(Number1,Operations[OperationNo],Number2)

    #Creating the correct answer (Depending on operation)
    if OperationNo == 0:
        Answer= Number1 * Number2
    if OperationNo == 1:
        Answer= Number1 + Number2
    if OperationNo == 2:
        Answer= Number1 - Number2

    #Adding the correct answer to array
    CorrectAnswer.append(Answer)
    
    #User input answer
    GivenAnswer= int(input("What is your answer?"))

    #Checking if Answer correct
    if GivenAnswer == CorrectAnswer[len(CorrectAnswer)-1]:
        #Adding to total score
        TotalCorrect = TotalCorrect +1
        print("Correct")
    if not(GivenAnswer == CorrectAnswer[len(CorrectAnswer)-1]):
        print("Incorrect")

#Printing total
print("Congratulations", Name, "you got", TotalCorrect, "out of 10")
        
    
