#sentence world replacer
######################################################
def SentenceReplacer(Sentence,Phrase):
    
    NumberOfTimes = Sentence//len(Phrase)
    Remainder = Sentence%len(Phrase)

    FinalSentence = []
    for x in range (0,NumberOfTimes):
        FinalSentence.append(Phrase) 
    for y in range (0,Remainder):
        FinalSentence.append(Phrase[y])
    #Empty array for final sentence
    
    print(''.join(FinalSentence))

######################################################

FilePlace = input("What is the location of the file?")
text_file = open((FilePlace),"r")
#Original sentence
Sentence = []

for line in text_file:
    for x in range (0,(len(line))):
        Sentence.append(line[x])

Sentencelen= len(Sentence)
#Phrase to replace it with
Phrase= input("Please give me a phrase to use")

SentenceReplacer((Sentencelen),(Phrase))


#Repeating whole phrase


