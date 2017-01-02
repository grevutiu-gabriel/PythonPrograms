#Importing time function
import time

#Program to total two teams scores
Player = []

#Checking how big to make thew array
PlayerTotal=int(input("How many players are there?"))
TeamNumber=int(input("How many Teams are there? (Max 4)"))
print("\n")

#Highscore variable
HighScore=0
HighScoreOwner = 0
InputNumber = 1
#Populating the array
for x in range(0,PlayerTotal):
    print("____________________________________________")
    PlayerName = input("What is your name?")

    print("What team were you on ",PlayerName ,"?")
    Team = input()

    #Green team = 1 or A | Red team = 2 or B | Yellow team = 3 or D | Blue team = 4 or D
    #Turning team names into A or B
    if Team.lower() == "green":
        Team = "A"
    if Team.lower() == "red":
        Team = "B"
    if Team.lower() == "yellow":
        Team = "C"
    if Team.lower() == "blue":
        Team = "D"

    #Turning numbers into A or B so as not to confuse scores
    if "1" in Team:
        Team= "A"
    if "2" in Team:
        Team= "B"
    if "3" in Team:
        Team= "C"
    if "4" in Team:
        Team= "D"

    if Team== "A" or Team== "B" or Team== "C" or Team== "D":  
        print("What score did you get ", PlayerName, "?")    
        score = int(input())

        #checking whether high-score
        if score > HighScore:
            HighScore = score
            HighScoreOwner = PlayerName

        #If score same as high score
        elif score == HighScore:
            HighScore = score
            HighScoreOwner = PlayerName ,"and", HighScoreOwner
            
        
        Player.append([Team,score])
        InputNumber = InputNumber +1
    else:
        print("That's not a valid team, try again")

    print("\n")
#making variables      
Team1Total= 0
Team2Total= 0
Team3Total= 0
Team4Total= 0
PlayerNumber= 0

#Totalling team scores
for y in range (0,len(Player)):
    #Checking which team the score belongs to
    if "A" in Player[PlayerNumber][0]:
        Team1Total= Team1Total + int(Player[PlayerNumber][1])
    if "B" in Player[PlayerNumber][0]:
        Team2Total= Team2Total + int(Player[PlayerNumber][1])
    if "C" in Player[PlayerNumber][0]:
        Team3Total= Team3Total + int(Player[PlayerNumber][1])
    if "D" in Player[PlayerNumber][0]:
        Team4Total= Team4Total + int(Player[PlayerNumber][1])
        
    #Iterating PlayerNumber
    PlayerNumber= PlayerNumber +1


#suspense delay
print("Calculating")
time.sleep(1)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")



#Displaying totals    
print("Green team got ", Team1Total)

#Suspense delay
time.sleep(1)
print(".")
time.sleep(1)
print("..")
time.sleep(1)
print("...")

#displaying totals
print("Red team got ",Team2Total)
time.sleep(1)
if TeamNumber == 3 or TeamNumber == 4:
    #Suspense delay
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")

    
    print("Yellow team got ",Team3Total)
    time.sleep(1)
if TeamNumber == 4:
    #Suspense delay
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")

    
    print("Blue team got ",Team4Total)
    time.sleep(1)

print("\n")

#Working out which team won
print("The winning team is")
print("\n")
if Team1Total > max(Team2Total,Team3Total,Team4Total):
      print("GREEN TEAM")
      
if Team2Total > max(Team1Total,Team3Total,Team4Total):
      print("RED TEAM")
      
if Team3Total > max(Team1Total,Team2Total,Team4Total):
      print("YELLOW TEAM")
      
if Team4Total > max(Team1Total,Team2Total,Team3Total):
      print("BLUE TEAM")


if Team1Total == Team2Total:
    print("It's a draw!")
time.sleep(5)

print("\n")

#Showing the top player/players
print("The highest scorer was",HighScoreOwner, "with a score of", HighScore)

