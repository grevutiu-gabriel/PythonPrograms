#Sentence alternate worder
#Sentence breakdown

#input Sentence to breakdown
Sentence= (input("What sentence would you like analysed?")).upper()

#Breking down and choosing letters
y=1       
while y in range (1,len(Sentence)):
    print(Sentence[y])
    y= y+2
