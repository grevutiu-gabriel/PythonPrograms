#Sentence compactor 2.0
WordsInside= []
WordsFound = 0
NumberFound = 0
Locations = []
#Breaking phrase into individual words (using spaces)
Phrase = ((input("What phrase would you like?")).upper()).split(" ")


#Repeating for each letter in phrase
for i in range (0,len(Phrase)):
    #checking each word against the word to find
    for Words in range (0,(len(WordsInside))):
        #If word is the same as word in phrase
        if WordsInside[Words] == Phrase[0] :
            
            #Printing word and position
            print("There is an ", Phrase[0], "at position", (Words +1))
            Locations.append((Words +1))
            
            #Has word been found
            WordsFound = 1
            #Stopping loop if word found
            Words = (len(WordsInside))

            #Adding to the counter that another word has been found
            NumberFound = NumberFound +1
            
    #If the word is not already found                    
    if WordsFound == 0:
        #Adding the word to the array
        WordsInside.append(Phrase[0])
        
        #Printing word and position
        print("There is a ", Phrase[0], "at position", (i +1 -NumberFound))

        #Adding location of word to array
        Locations.append((i +1 - NumberFound))
    WordsFound = 0
    Words = 0

    #removing word checked    
    Phrase.pop(0)

#Opening text file and inputtting all information required to rebuild the sentence
text_file = open("CompactedSentence.txt", "w")
text_file.write(str(WordsInside))
text_file.write("\n")
text_file.write(str(Locations))
text_file.close()

#printing array of words found
print(WordsInside)
print(Locations)
#She sells sea shells on the sea floor

