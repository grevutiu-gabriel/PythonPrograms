#Scrabble 


#Scrabble letter value array
Scores = [   [ "A", 1],
             [ "B", 3],
             [ "C", 3],
             [ "D", 2],
             [ "E", 1],
             [ "F", 4],
             [ "G", 2],
             [ "H", 4],
             [ "I", 1],
             [ "J", 8],
             [ "K", 5],
             [ "L", 1],
             [ "M", 3],
             [ "N", 1],
             [ "O", 1],
             [ "P", 3],
             [ "Q", 10],
             [ "R", 1],
             [ "S", 1],
             [ "T", 1],
             [ "U", 1],
             [ "V", 4],
             [ "W", 4],
             [ "X", 8],
             [ "Y", 4],
             [ "Z", 10]]

#Asking for word and splitting it up into individual characters (in capital)
Word= (input("What is your word?")).upper()

#Turning word into array (split into individual characters
Phrase = list(Word)

#initialising variables for word multiplyer and word total
Multiplyer = 1
TotalWord = 0

#Looping through entire word
for x in range(0,len(Phrase)):

    #Checking for Word multipliyer (only on first character
    if Phrase[x] == "3" and x==0:
        Multiplyer = 3

    if Phrase[x] == "2" and x==0:
        Multiplyer = 2
    
    #Checking if letter after is a character multiplyer
    try:
        #if the letter does not have a multiplyer after
        if not Phrase[x+1] == ("2" or "3"):
            #Checking value of letter in array
            for y in range (0,len(Scores)):
                if Scores[y][0] == Phrase[x]:
                    #Adding the score to total
                    TotalWord = TotalWord + Scores[y][1]
                    
        #If the letter does have a multiplyer (of 2)
        if Phrase[x+1] == ("2"):
            #Checking value in array
            for y in range (0,len(Scores)):
                if Scores[y][0] == Phrase[x]:
                    #Adding to total after multiplying
                    TotalWord = TotalWord + (Scores[y][1] * 2)

        #If the letter does have a multiplyer (of 3)                
        if Phrase[x+1] == ("3"):
            for y in range (0,len(Scores)):
                #Checking value of letter in array
                if Scores[y][0] == Phrase[x]:
                        #Adding to total after multiplying
                        TotalWord = TotalWord + (Scores[y][1] * 3)
                        
    #if the character is the last in the word (so cannot have a modifyer                    
    except:
        for y in range (0,len(Scores)):
            #Checking value of letter in array
                if Scores[y][0] == Phrase[x]:
                    TotalWord = TotalWord + Scores[y][1]

#Adding the multiplyer to the word        
TotalWord= TotalWord * Multiplyer
print(TotalWord)
