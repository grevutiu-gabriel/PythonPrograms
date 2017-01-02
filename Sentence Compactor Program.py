#Sentence compactor
WordsInside= []
location= []
WordsFound = 0
NumberFound = 0
Phrase = ((input("What phrase would you like?")).upper()).split(" ")
PhraseLen= len(Phrase)
#Repeating for each letter in phrase
for i in range (0,len(Phrase)):
    print(Phrase)
    #checking each word against the word to find
    for j in range (0,(len(WordsInside))):
        if WordsInside[j] == Phrase[0] :
            #If word == word in phrase
            #Printing word and position
            print("There is an ", Phrase[0], "at position", (i +1))
            WordsFound = 1
            NumberFound = NumberFound +1
            j = (len(WordsInside))+1
            
        if WordsFound == 1:
            WordsFound = WordsFound /2
            print("fail")
                        
    if WordsFound > 0:
        WordsInside.append(Phrase[0])
        print("There is a ", Phrase[0], "at position", (i +1))
        WordFound = 0
        if len(Phrase) == 1:
            if WordsInside[j] == Phrase[0] :
                #If word == word in phrase
                #Printing word and position
                print("There is an ", Phrase[0], "at position", (i +1))
                WordFound = 1
                NumberFound = NumberFound +1
    print(PhraseLen)
        
    Phrase.pop(0)
print(WordsInside)

#She sells sea shells on the sea floor
#+ NumberFound
