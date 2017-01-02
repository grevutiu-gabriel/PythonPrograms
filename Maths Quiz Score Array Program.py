#MathsQuiz Score array
file = open("MathsQuiz.txt", "r")
#Arrays for scores
Team1Scores= []
Team2Scores= []
ErrorTeam=[]

#Breaking down text file into array
Line1= (''.join(file.readlines(0))).split(" ")
Line1.pop()

for x in range(0,int((len(Line1))/3)):
    #Deciding which team they're in
    if Line1[0] == "1":
        Team1Scores.append((Line1[1],Line1[2]))
    if Line1[0] == "2":
        Team2Scores.append((Line1[1],Line1[2]))
    if not(Line1[0] == "1") and not(Line1[0] == "2"):
        ErrorTeam.append((Line1[0],Line1[1],Line1[2]))
    #Removing their data from array
    for y in range(0,3):
        Line1.pop(0)
    

print("Team1", Team1Scores)
print("Team2",Team2Scores)
print("No team", ErrorTeam)
print(Line1)

        
    
        
