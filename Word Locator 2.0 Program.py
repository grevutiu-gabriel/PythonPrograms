#Word locator 2
#Array for each word that appears
Words=[]
#Array for Location of word required to rebuild sentence in array
Location=[]

#asking for a phrase and making it upper case, then spilliting it into an array using the spaces
Phrase = ((input("What phrase would you like?")).upper()).split(" ")

#For each word in the phrase
for i in range (0, len(Phrase)):
    #resetting whther word was found
    Found = 0
    #Checking each word in Words against the word in phrase testing
    for y in range (0, (len(Words))):
        #If Word in phrase is in Words array
        if Words[y] == Phrase[i]:
            #Plot location in location array (+1 so it works logically to user)
            Location.append((y + 1))
            #Stating that word has been found in array
            Found = 1

    #If phrase word not found in array
    if Found == 0:
        #Add phrase word to array
        Words.append(Phrase[i])
        #Add location to location array (As it has been put on the end of array the location is array length)
        Location.append((len(Words)))

#Outputting words array and location    
print(Words)
print(Location)
