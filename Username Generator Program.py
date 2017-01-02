#Username generator
#Pre-existing username array
UserNames = ["DaRiggs98","DaRiggs981"]

#Required information for username generation
FirstName = input("What is your first name")
LastName = input("What is your last name")
DOB = input("in what year were you born?")

#Initialising variables
Username = ""
Repeat = ""

#Checking if first name long enough for 2 characters to be used
if (len(FirstName) < 2):
    
    Username = FirstName + LastName + DOB[-2:]

else:
    #Creating username
    Username = FirstName[:2] + LastName + DOB[-2:]

#Checking if username is pre-existing and adding the first free number    
while (Username + str(Repeat)) in UserNames:
    #making Repeat into an integer
    if Repeat == "":
        Repeat = 0
    #incrementing Repeat
    Repeat = Repeat +1

#If no repeats happened 
if Repeat == 0:
    UserNames.append(Username)
#If repeats happened
if  not Repeat == 0: 
    UserNames.append(Username + str(Repeat))
print(UserNames)    
