#Geography quiz
#Asking how many questions
NumberOfQuestions= round(int(float((input("How many questions would you like?")))))
print(NumberOfQuestions)
if NumberOfQuestions <= 0:
    NumberOfQuestions = 1
#Arrays for city and capital
QuestionsCity= []
QuestionsCountry= []
#initialising variables
CapitalCity = ""
Country= ""
Points = 0

#Getting questions and answers
for x in range(0,NumberOfQuestions):
    #Getting country and city and making it lower
    Country = (input("What is the country?")).lower()
    CapitalCity = (input("What is the capital city")).lower()
    #Adding city and country to relavent array
    QuestionsCountry.append(Country)
    QuestionsCity.append(CapitalCity)

#Stopping people looking at inputted questions
for y in range(0,100):
    print("No Cheat")

#Asking each question    
for n in range(0,len(QuestionsCity)):
    #Getting answer
    Answer= input(("What is the capital of", QuestionsCountry[n]))
    #Checking if correct
    if Answer in (QuestionsCity[n]):
        print("correct, 3 points")
        Points = Points + 3
    #If incorrect
    else:
        Answer= input(("incorrect, try again"))
        if Answer in (QuestionsCity[n]):
            print("correct, 2 points")
            Points = Points + 2
        else:
            Answer= input(("incorrect, try again"))
            if Answer in (QuestionsCity[n]):
                print("correct, 1 points")
                Points = Points + 1
            else:
                #Printing incorrect and the correct answer
                print("incorrect, the correct answer is ", QuestionsCity[n])
#Printing end score
print("Your score was", Points)
