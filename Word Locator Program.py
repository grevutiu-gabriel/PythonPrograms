#Word locator

#Vowel array
Wordtofind = input("What word would you like to find?").upper()

#asking for a phrase and making it upper case
Phrase = ((input("What phrase would you like?")).upper()).split(" ")
print(Phrase)

#Repeating for each letter in phrase
for i in range (0,len(Phrase)):
    #checking each word against the word to find
    if Wordtofind == Phrase[i]:
        #If word == word in phrase
        #Printing word and position
         print("There is a ", Wordtofind, "at position", (i +1))




