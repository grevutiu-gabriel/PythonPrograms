#Maths quiz +Class database
import random
text_file = open("MathsQuiz.txt", "w")
text_file.close()
Operations= ["*","+","-"]
TotalNumber= 3 #int(input("how many people will be doing this quiz?"))
for y in range(0,TotalNumber):
    Name = input("What is your name?")
    Class = input("What class number are you (e.g. 1)?")
    
    CorrectAnswer= []
    TotalCorrect = 0
    #Creating 10 questions and checking
    for x in range(0,1):
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
        try:
            GivenAnswer= int(input("What is your answer?"))
        except:
            GivenAnswer= -1000000
            print("ERROR: Number not recognised")

        #Checking if Answer correct
        if GivenAnswer == CorrectAnswer[len(CorrectAnswer)-1]:
            #Adding to total score
            TotalCorrect = TotalCorrect +1
            print("Correct")
        if not(GivenAnswer == CorrectAnswer[len(CorrectAnswer)-1]):
            print("Incorrect")
            
    text_file = open("MathsQuiz.txt", "a")
    text_file.write(Class + " " + Name + " " + str(TotalCorrect) + " ")
    text_file.close()

    #Printing total
    print("Congratulations", Name, "you got", TotalCorrect, "out of 10")
        
    
