#Sentence breakdown and randomiser
import random



########################################################################
########################################################################
def SentenceBreakdown(Sentence):
    #Defining arrays
    Alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    Letter = []
    newSentence=[]
    
    for i in range (0,len(Sentence)):
        #Checking whether letter is in alphabet
        for x in range(0,len(Alphabet)):
            #checking letter
            if Alphabet[x] in Sentence[i]:
                #incrementing count and adding to letter
                Letter.append(Alphabet[x])

    #Choosing letters at random from array and printing them        
    for y in range (0,len(Letter)):
        letterChosen=random.randint(0,(len(Letter)-1))

        #Putting in an array so it prints on same line
        newSentence.append(Letter[letterChosen])
        
        #removing last letter so is not repeated
        del Letter[letterChosen]

    #Amalgamating array and printing letters    
    print(''.join(newSentence))

########################################################################
########################################################################

        
#input Sentence to breakdown
Sentence= (input("What sentence would you like analysed?")).upper()
SentenceBreakdown(Sentence)
