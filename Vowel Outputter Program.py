#Vowel outputter

#Vowel array
Vowels = ["A","E","I","O","U"]

#variables for vowel count
aCount=0
eCount=0
iCount=0
oCount=0
uCount=0

#asking for a phrase and making it upper case
Phrase = (input("What phrase would you like?")).upper()

#Repeating for each letter in phrase
for i in range (0,len(Phrase)):
    #checking each letter against each vowel
    for j in range(0,len(Vowels)):
        #If letter = a vowel
        if Phrase[i] in Vowels[j]:
            #Printing vowel and position
            print("There is an", Vowels[j], "at position", (i +1))

            #Adding to relevent vowel count
            if j == 0:
                aCount= aCount +1

            if j == 1:
                eCount= eCount +1

            if j == 2:
                iCount= iCount +1

            if j == 3:
                oCount= oCount +1
            if j == 4:
                uCount= uCount +1


#printing vowel counts
print("There were", aCount, "A's")
print("There were", eCount, "E's")
print("There were", iCount, "I's")
print("There were", oCount, "O's")
print("There were", uCount, "U's")
