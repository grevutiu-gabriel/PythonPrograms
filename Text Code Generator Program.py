#Text code generator

Alphabet = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

Reverse = input("Would you like to input a Coded word?")

#Generating numerical value for code word
Code = input("What is your code-word?")
    
#Breaking code into characters, turning them into numbers, then adding them up
CodeNumber= sum([ord(i) for i in Code])

if "y" in Reverse.lower():
    CodeNumber= CodeNumber*-1

print(CodeNumber)
#Getting code word
Word= (str(input("What is the word you want converted?"))).upper()

NewWord = []

#Converting to number and adding code number
for x in range(0,(len(Word))):
    #Calculating the number the letter is
    LetterNumber = ((ord(Word[x]))+ CodeNumber)
    #Making sure letter is in range of array
    while LetterNumber > 36:
        LetterNumber = LetterNumber - 36
        print("1")
        
    while LetterNumber < 0:
        LetterNumber = LetterNumber + 36
    #Converting back to letter and adding to newword    
    NewWord.append(Alphabet[LetterNumber])

print(''.join(NewWord))


