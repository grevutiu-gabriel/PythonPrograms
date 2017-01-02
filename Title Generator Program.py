#Name and title stater

#Declaring and inputting needed data
Name= input("What is your name?")
Gender= input("What is your gender?")
Married= input("Are you married?")

#Defining subroutine
def TitleGen(Name,Gender,Married):
    #Checking if female
    if "f" in Gender.lower():
        #Checking marital status
        if "y" in Married.lower():
            print("Mrs", Name)
        else:
            print("Miss", Name)     
    else:
        print("Mr", Name)

#Calling up subroutine
TitleGen(Name,Gender,Married)
